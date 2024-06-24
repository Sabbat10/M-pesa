# import currency

from USD.curency.usd import usd
from FC.curency.fc import fc

def faire_choix():
    
    while True:
        print() 
        choix_str = input("Vielles selectionner \n1. Compte M-pesa USD\n2. Compte M-pesa FC\n3. Inviter un proche\n4. Balance Rallonge (gratuit)\n5. Compte Bonus\nChoix : ")
        try:
            choix = int(choix_str)
            if choix == 1:
                usd()
                break
            elif choix == 2:
                fc()
                break
            elif choix == 3:
                print("choix 3")
                break
            elif choix == 4:
                print("Choix 4")
                break
            elif choix == 5:
                print("Choix 5") 
                break       
            else:
                print()
                print("Choix invalide. Veuillez saisir un nombre entre 1 et 5.")
        except ValueError:
            print("Saisie invalide. Veuillez saisir un nombre.")
    
    return choix

faire_choix()