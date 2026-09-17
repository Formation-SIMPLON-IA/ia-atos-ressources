"""Génère le dataset de fine-tuning (tickets SAV NovaThread -> résumé JSON) — reproductible."""
import json
import random
from pathlib import Path

OUT = Path(__file__).resolve().parent
OUT.mkdir(parents=True, exist_ok=True)
random.seed(42)

CATEGORIES = ["livraison", "produit_defectueux", "remboursement", "taille_ou_ajustement",
              "paiement", "compte_client", "autre"]
URGENCES = ["basse", "moyenne", "haute"]

# briques de texte pour fabriquer des tickets réalistes et variés
OUVERTURES = [
    "Bonjour, ", "Bonjour,\n", "Hello, ", "Coucou, ", "Madame, Monsieur, ",
    "", "Salut, ", "Bjr ", "Bonsoir, ",
]
PRODUITS = ["robe été fleurie", "veste en lin", "jupe midi plissée", "pull col roulé",
            "pantalon chino", "chemisier soie", "manteau laine", "paire de bottines"]
CORPS = {
    "livraison": [
        "je n'ai toujours pas reçu ma commande passée il y a {n} jours. Le suivi indique 'en transit' depuis une semaine.",
        "ma commande était censée arriver lundi mais rien. C'est urgent, c'est pour un mariage samedi !",
        "le colis a été marqué livré mais je n'ai rien reçu dans ma boîte aux lettres.",
        "cela fait {n} jours et aucune nouvelle de mon colis, je commence à m'inquiéter.",
    ],
    "produit_defectueux": [
        "la {produit} que j'ai reçue a une couture décousue au niveau de l'épaule.",
        "il y a un trou dans le tissu de la {produit}, visiblement un défaut d'usine.",
        "la fermeture éclair de la {produit} est cassée dès le premier essayage.",
        "la {produit} a déteint au premier lavage alors que j'ai suivi les instructions.",
    ],
    "remboursement": [
        "j'ai renvoyé la {produit} il y a trois semaines et je n'ai toujours pas été remboursée.",
        "je souhaite être remboursée intégralement, l'article ne me convient pas du tout.",
        "on m'a promis un remboursement sous 14 jours, cela fait un mois maintenant.",
    ],
    "taille_ou_ajustement": [
        "la {produit} taille beaucoup trop petit, je voudrais échanger contre une taille au-dessus.",
        "j'ai commandé du M mais on dirait du XS, comment faire un échange ?",
        "les mensurations sur le site ne correspondent pas du tout à la réalité.",
    ],
    "paiement": [
        "j'ai été débitée deux fois pour la même commande, merci de corriger rapidement.",
        "mon code promo n'a pas été appliqué au moment du paiement.",
        "le paiement a échoué mais j'ai quand même été débitée.",
    ],
    "compte_client": [
        "impossible de me connecter à mon compte, le lien de réinitialisation n'arrive jamais.",
        "je voudrais supprimer mon compte et toutes mes données personnelles.",
        "mon historique de commandes a disparu de mon espace client.",
    ],
    "autre": [
        "je voulais juste vous féliciter pour la qualité de vos emballages, c'est top !",
        "avez-vous prévu de réassortir la {produit} en bleu marine bientôt ?",
        "est-il possible d'avoir une facture avec le nom de mon entreprise ?",
    ],
}
# Réservés au test : aucune de ces formulations ne doit apparaître à l'entraînement.
# Le test vérifie ainsi la règle métier sur des formulations inédites, pas la
# mémorisation d'un gabarit vu pendant le fine-tuning.
CORPS_TEST = {
    "livraison": [
        "où en est mon envoi ? Il aurait dû arriver depuis {n} jours et je n'ai rien.",
        "le transporteur annonce une livraison effectuée, pourtant aucun colis n'est chez moi.",
    ],
    "produit_defectueux": [
        "à l'ouverture, j'ai constaté que la {produit} était abîmée et inutilisable.",
        "ma {produit} présente un défaut après une seule utilisation.",
    ],
    "remboursement": [
        "mon retour a bien été réceptionné mais le remboursement n'apparaît toujours pas.",
        "je veux savoir quand sera crédité le montant de l'article retourné.",
    ],
    "taille_ou_ajustement": [
        "la coupe de la {produit} ne correspond pas ; puis-je la remplacer par une autre taille ?",
        "l'article reçu est trop grand et je souhaite procéder à un échange.",
    ],
    "paiement": [
        "ma carte a été prélevée, mais la commande semble ne pas avoir été validée.",
        "une même facture apparaît deux fois sur mon relevé bancaire.",
    ],
    "compte_client": [
        "je ne reçois pas l'e-mail nécessaire pour retrouver l'accès à mon espace personnel.",
        "je souhaite effacer mon profil client et les informations qui y sont associées.",
    ],
    "autre": [
        "pourriez-vous me dire si la {produit} sera prochainement à nouveau disponible ?",
        "j'aurais besoin d'un justificatif d'achat au nom de mon employeur.",
    ],
}
FERMETURES = [
    " Merci d'avance.", " Cordialement.", " Bien à vous.", " Merci de faire le nécessaire.",
    "", " Dans l'attente de votre retour.", " Répondez vite svp.", " Merci beaucoup !!",
]
# indices d'urgence: présence de marqueurs -> haute ; ton neutre -> moyenne ; compliment/info -> basse
MARQUEURS_HAUTE = ["urgent", "mariage samedi", "rapidement", "vite", "débitée deux fois", "s'inquiéter"]


def urgence_de(categorie: str, corps: str) -> str:
    txt = corps.lower()
    if categorie == "autre":
        return "basse"
    if any(m in txt for m in MARQUEURS_HAUTE):
        return "haute"
    if categorie in ("produit_defectueux", "remboursement", "paiement"):
        return "moyenne"
    return "moyenne"


def resume_de(categorie: str, produit: str) -> str:
    modeles = {
        "livraison": "Colis non reçu / retard de livraison",
        "produit_defectueux": f"Défaut produit sur {produit}",
        "remboursement": "Demande de remboursement en attente",
        "taille_ou_ajustement": f"Problème de taille, échange souhaité ({produit})",
        "paiement": "Anomalie de paiement",
        "compte_client": "Problème d'accès ou de données du compte",
        "autre": "Message d'information ou compliment",
    }
    return modeles[categorie]


def fabrique_ticket(corps_par_categorie: dict[str, list[str]] = CORPS) -> dict:
    categorie = random.choice(CATEGORIES)
    produit = random.choice(PRODUITS)
    gabarit = random.choice(corps_par_categorie[categorie])
    corps = gabarit.format(produit=produit, n=random.choice([5, 8, 10, 12, 15]))
    texte = random.choice(OUVERTURES) + corps + random.choice(FERMETURES)
    cible = {
        "categorie": categorie,
        "urgence": urgence_de(categorie, corps),
        "resume": resume_de(categorie, produit),
    }
    return {"ticket": texte.strip(), "sortie": cible}


INSTRUCTION = (
    "Tu es l'assistant de tri du SAV NovaThread. Résume le ticket client en JSON "
    "avec exactement ces clés : \"categorie\" (une valeur parmi "
    "livraison, produit_defectueux, remboursement, taille_ou_ajustement, paiement, "
    "compte_client, autre), \"urgence\" (basse, moyenne ou haute), \"resume\" (une "
    "phrase courte). Réponds UNIQUEMENT avec le JSON."
)


def en_exemple_chat(ex: dict) -> dict:
    return {"messages": [
        {"role": "system", "content": INSTRUCTION},
        {"role": "user", "content": ex["ticket"]},
        {"role": "assistant", "content": json.dumps(ex["sortie"], ensure_ascii=False)},
    ]}


tous = [fabrique_ticket() for _ in range(360)]
# dédoublonnage sur le texte
vus, uniques = set(), []
for ex in tous:
    if ex["ticket"] not in vus:
        vus.add(ex["ticket"])
        uniques.append(ex)

train = uniques
test = [fabrique_ticket(CORPS_TEST) for _ in range(60)]

(OUT / "train.jsonl").write_text(
    "\n".join(json.dumps(en_exemple_chat(e), ensure_ascii=False) for e in train), encoding="utf-8")
(OUT / "test.jsonl").write_text(
    "\n".join(json.dumps(e, ensure_ascii=False) for e in test), encoding="utf-8")
(OUT / "instruction.txt").write_text(INSTRUCTION, encoding="utf-8")

print(f"train : {len(train)} exemples (format chat) -> train.jsonl")
print(f"test  : {len(test)} exemples hors gabarits train (ticket + sortie attendue) -> test.jsonl")
from collections import Counter
print("répartition catégories (tout) :", dict(Counter(e["sortie"]["categorie"] for e in uniques)))
print("répartition urgences (tout)   :", dict(Counter(e["sortie"]["urgence"] for e in uniques)))
print("\nexemple train :", json.dumps(en_exemple_chat(train[0]), ensure_ascii=False)[:300])
print("\nexemple test  :", json.dumps(test[0], ensure_ascii=False)[:200])
