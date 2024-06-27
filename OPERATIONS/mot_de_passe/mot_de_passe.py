mot_de_passe = 123456

def mot_de_passe():
    while True:
        print()
        mot_de_passe_str = input("Inserer votre PIN M-PESA (4 à 6 chiffres)\nGadez-le secret\n00. Retour : ")
        try:
            mot_de_passe = int(mot_de_passe_str)
            if mot_de_passe == 123456:
                print("Mot de passe correct")
                break
            else:
                print("Mot de passe incorrect")
        except ValueError:
            print("Saisie invalide. Veuillez entrer un mot de passe valide.")
    
    return mot_de_passe                