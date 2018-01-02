# -*-coding:Utf-8 -*

"""Ce module contient les fonctions permettant de se déplacer dans le labyrinthe"""

def labyrinthe(carte): 
    import pickle
    import os
    print("N pour allez au nord, S pour aller au sud")
    print("E pour allez à l'est, O pour allez à l'ouest")
    print("indiquer un nombre après la direction pour avancer de plusieurs cases")
    print("Q pour quitter")
    print(carte)
    while True:
        win = False
        choix = input("choisir une direction:")
        if len(choix) > 1:
            try:
                iteration = int(choix[1:])
            except:
                iteration = 1
        else:
            iteration = 1
        if choix[0] == "Q":
            print("fin du jeu")
            break
        while iteration > 0:
            if carte.deplacement(choix[0])=="WIN":
                win = True
            iteration = iteration - 1
        if win == True:
            print("Bravo ! C'est gagné")
            os.remove(os.path.join("sauvegarde","sauvegarde.txt"))
            break
        else:
            print("-------------------")
            print(carte)
            print("-------------------")
            with open(os.path.join("sauvegarde","sauvegarde.txt"), "wb") as sauvegarde:
                pickle.Pickler(sauvegarde).dump(carte)    
