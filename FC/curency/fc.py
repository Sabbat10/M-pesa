from retire_du_cash.retirer_du_cash import retirer_du_cash

def fc():
    
    while True:
        print() 
        choix_str = input("Compte M-pesa FC \n1. Envoie Argent\n2. Achat Credit ou Forfaits\n3. Retirer du Cash\n4. Services Financiers\n5. Mes Paiements\n6. Bureau de Change\n7. Services Compte\n8. Retour\nChoix :  ")
        try:
            choix = int(choix_str)
            if choix in [1, 2, 3, 4, 5]:
                retirer_du_cash()
                break
            else:
                print("Choix invalide. Veuillez saisir un nombre entre 1 et 5.")
        except ValueError:
            print("Saisie invalide. Veuillez saisir un nombre.")
    
    return choix