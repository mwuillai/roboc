#!/pi/bin/env python3
# -*-coding:Utf-8 -*

import os

"""Ce module contient la classe Carte."""

class Carte:

    """Objet de transition entre un fichier et un labyrinthe."""
    grille={}
    x=0 #variable dynamique indiquant la position x de la case en cours d'insertion
    y=0 #variable dynamique indiquant la position x de la case en cours d'insertion
    X=(0,0) #position du joueur dans le labyrinthe
    longueur=0 #longueur du labyrinthe
    mvtprecedent=" " #contient le contenu de la case ou se trouvait x avant le déplacement
    
    def __init__(self,nom,dossier,chaine):
        """Initialisation du labyrinthe à partir du fichier carte affecte une position x et y à chaque caractère du labyrinthe"""
        with open(os.path.join(dossier,"{}.txt".format(chaine)),"r") as laby:
            labyBrut = laby.readline()
            self.longueur= len(labyBrut)
            labyBrut+=laby.read()
            grille={}
            for i,case in enumerate(labyBrut):
                self.calcxy(i)
                grille[self.x,self.y]=case
                self.posX(self.x,self.y,case)
        self.nom = nom
        self.grille = grille

    def posX(self,axex,axey,value):
        """Définis la position de X à utiliser à chaque mouvement du joueur pour actualiser sa position"""
        if value == "X":
            self.X=(axex,axey)

    def calcxy(self,i):
        """Calcul x et y en fonction de la longueur du labyrinthe fonction à utiliser dans le cadre d'une boucle pour mettre à jour l'attribut à chaque affectation de case"""
        self.x=i-(i//self.longueur)*self.longueur
        self.y=i//self.longueur

    def __repr__(self):
        grille_complete=""
        for i,case in enumerate(self.grille):
            self.calcxy(i)
            grille_complete += self.grille[self.x,self.y]
        return grille_complete

    """-------------------------------------------------------------------------------------------------------------------------------
    Définition des actions de déplacement, sur cette class carte j'insère également les actions permettant à un personnage de se déplacer.
    Cela se fera en 3 étapes, d'abord déclaration de l'intention du mouvement, vérification de la validité du mouvement, réalisation du mouvement.
    ----------------------------------------------------------------------------------------------------------------------------------"""
    def deplacement(self,orientation):
#        import pdb; pdb.set_trace()
        if orientation == "O":
            cible = (self.X[0]-1,self.X[1])
        elif orientation == "E":
            cible = (self.X[0]+1,self.X[1])
        elif orientation == "N":
            cible = (self.X[0],self.X[1]-1)
        elif orientation == "S":
            cible = (self.X[0],self.X[1]+1)
        else :
            return "Erreur : mauvaise saisie"
        etatcible = self.grille[cible]
        if etatcible == " " or etatcible == ".":
            self.grille[self.X]=self.mvtprecedent #L'emplacement de X prend la valeur du dernier mouvement
            self.mvtprecedent = etatcible #Le mouvement précédent devient la valeur de la case à venir
            self.grille[cible] = "X" #La valeur de la case cible devient X
            self.X=cible
        elif etatcible == "O":
            print("poum! Un mur ça fait mal")
        elif etatcible == "U":
            return "WIN"
