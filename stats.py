import matplotlib.pyplot as plt

def afficher_graphique_depenses(transactions):
    """Génère un camembert des dépenses par catégorie."""
    depenses_par_cat = {}

    for t in transactions:
        # Si la transaction vient du JSON, c'est un dictionnaire.
        # Si elle vient de l'objet Transaction, c'est un objet.
        montant = t.montant if hasattr(t, "montant") else t["montant"]
        categorie = t.categorie if hasattr(t, "categorie") else t["categorie"]

        if montant < 0:  # Uniquement les dépenses
            montant_abs = abs(montant)
            depenses_par_cat[categorie] = depenses_par_cat.get(categorie, 0) + montant_abs

    if not depenses_par_cat:
        print("Aucune dépense enregistrée pour afficher le graphique.")
        return

    categories = list(depenses_par_cat.keys())
    montants = list(depenses_par_cat.values())

    plt.figure(figsize=(6, 6))
    plt.pie(montants, labels=categories, autopct='%1.1f%%', startangle=140)
    plt.title("Répartition des Dépenses par Catégorie")
    plt.tight_layout()
    plt.show()