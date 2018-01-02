# -*-coding:Utf-8 -*

"""Ce fichier contient le code principal du jeu.

Exécutez-le avec Python pour lancer le jeu.

"""

import os

import pickle
from carte import Carte
from labyrinthe import labyrinthe

# On charge les cartes existantes
cartes = []
for nom_fichier in os.listdir("cartes"):
    if nom_fichier.endswith(".txt"):
        chemin = os.path.join("cartes", nom_fichier)
        nom_carte = nom_fichier[:-4].lower()
        cartes.append(nom_carte)

# Affichage des choix dans une boucle while 
while True:
    # On vérifie s'il y a une sauvegarde
    chemin_sauvegarde = os.path.join("sauvegarde","sauvegarde.txt")
    if os.path.isfile(chemin_sauvegarde) is True:
        sauvegarde = True
    else:
        sauvegarde = False

    print("Bienvenue dans Roboc !")
    print("Entrez le numéro d'un labyrinthe pour commencer une partie")
    print("Entrez 'q' pour quitter le jeu")
    if sauvegarde == True:
        print("Entrez 's' pour reprendre votre dernière partie")
    print("Labyrinthes existants :")
    for i, carte in enumerate(cartes):
        print("  {} - {}".format(i,carte))
    choix = input("Choisir un labyrinthe:")
    if choix == "q":
        print("A bientôt !")
        break
    elif choix == "s" and sauvegarde == True:
        with open(os.path.join("sauvegarde","sauvegarde.txt"),"rb") as sauvegarde:
            carte = pickle.Unpickler(sauvegarde).load()
        labyrinthe(carte)
        continue
    else:
        try:
            choix = cartes[int(choix)]
            carte = Carte(choix,"cartes",choix)
            labyrinthe(carte)
            continue
        except:
            print("erreur recommence la saisie")
            continue
