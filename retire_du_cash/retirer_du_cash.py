
def retirer_du_cash():
    
    while True:
        print() 
        choix_str = input("Retirer du Cash \n1. Retrait Aupres d'un Agent\n2. Retrait Au distributeur\n3. Retrait a la Banque\n4. Forfait Frais de Retrait\n5. Retour\n6\nChoix :  ")
        try:
            choix = int(choix_str)
            if choix in [1, 2, 3, 4]:
                print("Choix valide...")
                break
            elif choix == 5:
                print("Retour")
            else:
                print("Choix invalide. Veuillez saisir un nombre entre 1 et 5.")
        except ValueError:
            print("Saisie invalide. Veuillez saisir un nombre.")
    
    return choix