from models import PortfolioFinance

def afficher_menu():
    print("\n" + "="*30)
    print(" GESTIONNAIRE DE BUDGET ")
    print("="*30)
    print("1. Ajouter un revenu / dépense")
    print("2. Afficher l'historique")
    print("3. Simuler une épargne à terme")
    print("4. Quitter")

def main():
    nom = input("Entrez votre nom : ").strip()
    portefeuille = PortfolioFinance(nom)

    while True:
        afficher_menu()
        choix = input("\nChoisissez une option (1-4) : ").strip()

        if choix == "1":
            desc = input("Description : ")
            
            # Validation de la saisie
            try:
                montant = float(input("Montant (ex: 50 ou -20.5) : "))
            except ValueError:
                print("Erreur : Veuillez entrer un nombre valide.")
                continue

            cat = input("Catégorie (Ex: Salaire, Loyer, Nourriture) : ")
            portefeuille.ajouter_transaction(desc, montant, cat)

        elif choix == "2":
            print(f"\n--- Historique de {portefeuille.nom_utilisateur} ---")
            if not portefeuille.transactions:
                print("Aucune transaction enregistrée.")
            else:
                for t in portefeuille.transactions:
                    print(t)
            print(f"Solde total : {portefeuille.solde:.2f} €")

        elif choix == "3":
            try:
                epargne_mensuelle = float(input("Épargne mensuelle (€) : "))
                taux = float(input("Taux d'intérêt annuel (%) : "))
                annees = int(input("Durée (années) : "))
                portefeuille.simuler_epargne(epargne_mensuelle, taux, annees)
            except ValueError:
                print("Erreur de saisie dans les chiffres.")

        elif choix == "4":
            print("Merci d'avoir utilisé l'application. À bientôt !")
            break
        else:
            print("Option invalide, réessayez.")

if __name__ == "__main__":
    main()
    