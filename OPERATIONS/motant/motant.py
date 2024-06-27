from OPERATIONS.mot_de_passe.mot_de_passe import mot_de_passe
def motant():
    while True:
        print()
        motant_str = input("Montant \n00. Retour : ")
        try:
            motant = int(motant_str)
            if motant != motant:
                print("Entrer un motant valide !")
            else:
                mot_de_passe()    
            break
        except ValueError:
            print("Saisie invalide. Veuillez entrer un motant valide.")
    
    return motant