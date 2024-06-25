# importation de la fonction retirer_du_cash
from OPERATIONS.retire_du_cash.retirer_du_cash import retirer_du_cash

# fonction usd
def usd():
    
    while True:
        print() 
        choix_str = input("Compte M-pesa USD \n1. Envoie Argent\n2. Achat Credit ou Forfaits\n3. Retirer du Cash\n4. Services Financiers\n5. Mes Paiements\n6. Bureau de Change\n7. Services Compte\n8. Retour\nChoix :  ")
        try:
            choix = int(choix_str)
            if choix == 1:
                print("Choix valide usd")
                break
            elif choix == 2:
                print("Achat Credit ou Forfaits")
                break
            elif choix == 3:
                retirer_du_cash()
                break
            elif choix == 4:
                print("Services Financiers")
                break
            elif choix == 5:
                print("Mes Paiements")
                break
            elif choix == 6:
                print("Bureau de Change")
                break
            elif choix == 7:
                print("Services Compte")
                break
            elif choix == 8:
                break
            else:
                print("Choix invalide. Veuillez saisir un nombre entre 1 et 5.")
        except ValueError:
            print("Saisie invalide. Veuillez saisir un nombre.")
    
    return choix