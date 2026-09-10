"""Génère la version PDF imprimable des fiches de révision CISIA.

Le HTML est la source unique. Ce script en dérive une variante « papier » :
les repères de correction, repliés dans un ``<details>`` à l'écran, sont
déplacés en **annexe** de fin de document — sinon les auto-tests deviennent
une simple lecture, corrections sous les yeux.

Usage :
    python build_pdf.py            # → fiches-revision-cisia.pdf
    python build_pdf.py --keep-tmp # conserve le HTML intermédiaire (debug)

Dépendance : weasyprint (``brew install weasyprint`` ou ``pip install weasyprint``).
"""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
from pathlib import Path

HERE = Path(__file__).parent
SOURCE = HERE / "fiches-revision-cisia.html"
OUTPUT = HERE / "fiches-revision-cisia.pdf"

DETAILS_RE = re.compile(
    r"[ \t]*<details><summary>Repères de correction</summary>\s*(?P<corr>.*?)\s*</details>\n?",
    re.DOTALL,
)
SECTION_RE = re.compile(r'<section class="fiche[^"]*" id="(?P<sid>[^"]+)">')
H2_RE = re.compile(r"<h2>(?P<title>.*?)</h2>", re.DOTALL)

PRINT_CSS = """
  /* --- ajouts propres à la sortie PDF (injectés par build_pdf.py) --- */
  @page { size: A4; margin: 16mm 14mm 18mm; }
  @page { @bottom-center { content: counter(page) " / " counter(pages);
          font-size: 9pt; color: #6b7280; } }
  body { font-size: 10.5pt; }
  section.fiche { break-before: page; }
  section.fiche:first-of-type { break-before: auto; }
  h2, h3, h4 { break-after: avoid; }
  table, .callout, .autotest, .synthcard { break-inside: avoid; }
  .corrref { font-size: 9.5pt; font-style: italic; color: #6b7280; margin-top: 8px; }
  section.annexe .corr { margin-bottom: 14px; }
  section.annexe h3 { margin: 14px 0 4px; font-size: 13pt; }
"""


def build_print_html(html: str) -> str:
    """Retire les blocs de correction du corps et les regroupe en annexe.

    Args:
        html: le HTML source, tel qu'il est servi à l'écran.

    Returns:
        Le HTML de la variante papier, corrections déplacées en fin.
    """
    corrections: list[tuple[str, str]] = []

    # Titre de la fiche courante = dernier <h2> rencontré avant le <details>.
    def take(match: re.Match[str]) -> str:
        start = match.start()
        titles = H2_RE.findall(html[:start])
        title = titles[-1].strip() if titles else "Fiche"
        sids = SECTION_RE.findall(html[:start])
        sid = sids[-1] if sids else str(len(corrections) + 1)
        corrections.append((title, match.group("corr")))
        n = len(corrections)
        return (
            f'  <p class="corrref">→ Repères de correction : '
            f"annexe {n}, en fin de document (<em>{title}</em>).</p>\n"
        )

    body = DETAILS_RE.sub(take, html)
    if not corrections:
        raise SystemExit(
            "Aucun bloc « Repères de correction » trouvé — source modifiée ?"
        )

    blocks = "\n".join(
        f"  <h3>Annexe {i} — {title}</h3>\n  {corr}"
        for i, (title, corr) in enumerate(corrections, start=1)
    )
    annexe = (
        '\n<section class="fiche annexe" id="annexe">\n'
        '  <div class="fhead">\n'
        '    <span class="code">✔ Annexes</span>\n'
        "    <h2>Repères de correction</h2>\n"
        '    <div class="rt">À ne consulter qu\'après avoir répondu à voix haute</div>\n'
        "  </div>\n"
        f"{blocks}\n"
        "</section>\n"
    )

    # L'annexe se place après la dernière fiche, avant la fermeture du conteneur.
    marker = "\n</div>\n\n<footer>"
    if marker not in body:
        raise SystemExit("Structure inattendue : conteneur/footer introuvable.")
    body = body.replace(marker, f"{annexe}</div>\n\n<footer>", 1)

    return body.replace("</style>", f"{PRINT_CSS}</style>", 1)


def render(source: Path, output: Path) -> None:
    """Rend le HTML en PDF via weasyprint (module Python, sinon binaire).

    Args:
        source: HTML à rendre.
        output: chemin du PDF produit.

    Raises:
        SystemExit: si weasyprint n'est disponible sous aucune des deux formes.
    """
    try:
        from weasyprint import HTML

        HTML(filename=str(source)).write_pdf(str(output))
        return
    except ImportError:
        pass

    binary = shutil.which("weasyprint")
    if not binary:
        raise SystemExit("weasyprint introuvable → brew install weasyprint")
    subprocess.run([binary, str(source), str(output)], check=True)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--keep-tmp", action="store_true", help="conserver le HTML intermédiaire"
    )
    args = parser.parse_args()

    printable = build_print_html(SOURCE.read_text(encoding="utf-8"))
    tmp = HERE / "_print.html"
    tmp.write_text(printable, encoding="utf-8")

    try:
        render(tmp, OUTPUT)
    finally:
        if not args.keep_tmp:
            tmp.unlink(missing_ok=True)

    print(f"{OUTPUT.name} — {OUTPUT.stat().st_size // 1024} Ko")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
