
def usd():
    
    while True:
        print() 
        choix_str = input("Vielles selectionner \n1. Compte M-pesa USD\n2. Compte M-pesa FC\n3. Inviter un proche\n4. Balance Rallonge (gratuit)\n5. Compte Bonus\nChoix : ")
        try:
            choix = int(choix_str)
            if choix in [1, 2, 3, 4, 5]:
                print("Choix valide usd")
                break
            else:
                print("Choix invalide. Veuillez saisir un nombre entre 1 et 5.")
        except ValueError:
            print("Saisie invalide. Veuillez saisir un nombre.")
    
    return choix


def faire_choix():
    
    while True:
        print() 
        choix_str = input("Vielles selectionner \n1. Compte M-pesa USD\n2. Compte M-pesa FC\n3. Inviter un proche\n4. Balance Rallonge (gratuit)\n5. Compte Bonus\nChoix : ")
        try:
            choix = int(choix_str)
            if choix in [1, 2, 3, 4, 5]:
                usd()
                break
            else:
                print("Choix invalide. Veuillez saisir un nombre entre 1 et 5.")
        except ValueError:
            print("Saisie invalide. Veuillez saisir un nombre.")
    
    return choix

faire_choix()