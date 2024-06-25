
def retirer_du_cash():
    
    while True:
        print() 
        choix_str = input("Retirer du Cash \n1. Retrait Aupres d'un Agent\n2. Retrait Au distributeur\n3. Retrait a la Banque\n4. Forfait Frais de Retrait\n5. Retour\n6\nChoix :  ")
        try:
            choix = int(choix_str)
            if choix == 1:
                print("Retrait Aupres d'un Agent")
                break
            elif choix == 2:
                print("Retrait Au distributeur")
                break
            elif choix == 3:
                print("Retrait a la Banque")
                break
            elif choix == 4:
                print("Forfait Frais de Retrait")
                break
            elif choix == 5:
                print("Retour")
                break
            else:
                print("Choix invalide. Veuillez saisir un nombre entre 1 et 5.")
        except ValueError:
            print("Saisie invalide. Veuillez saisir un nombre.")
    
    return choix