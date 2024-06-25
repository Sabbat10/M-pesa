# function agent
numero_agent = 12345678
def agent():

    while True:
        print() 
        choix_str = input("Entrer Numéro Agent\n 00. Retour :  ")
        try:
            choix = int(choix_str)
            if choix == "":
                print("Entrer un mot de passe de 4 à 6 chiffres" )
                break
            elif choix == numero_agent:
                print("Veillez inserer un mot de passe")
                break
            elif choix == 00:
                break
            else:
                print("Choix invalide. Veuillez entrer un nombre.")
            
        except ValueError:
            print("Saisie invalide. Veuillez entrer un nombre.")
    
    return choix        