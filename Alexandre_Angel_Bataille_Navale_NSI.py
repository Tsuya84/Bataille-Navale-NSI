"""
                                ----------------------------------------------------------------
                                PROJECT NSI | ALEXANDRE CORREIA - ANGEL DIJOUX | BATAILLE NAVALE
                                ----------------------------------------------------------------

    main :    --------------------------------------------------------------------------------------------------------
              |  Bataille ->  __init__  [ Initialize the display with Tkinter, and initialize the                     |
              |                              "__demander_joueurs" and "__placer_bateaux" methods ]                    |
              |                                                                                                       |
              |               demander_joueurs  [ Initializes players and use joueur.py  ]                            |
              |                                                                                                       |
              |               __placer_bateaux    [ Initializes the boats according to the number of players ]        |
              |                                                                                                       |
              |               __lancer_partie     [ Call grille.py fenetre.py and case.py to start the game using     |
              |                                          "__demander_joueurs" and "__placer_bateaux" ]                |
              |                                                                                                       |
              |               demarrer            [ Start the game ]                                                  |
              --------------------------------------------------------------------------------------------------------
    
    joueur :    --------------------------------------------------------------------------------------------------------
                |  Joeur -> __init__ [ Initialize players ]                                                             |
                |                                                                                                       |
                |           ajouter_case_jouee   [ Add players box ]                                                    |
                |                                                                                                       |
                |           retirer_case_jouee   [ Remove player box ]                                                  |
                |                                                                                                       |
                |           placer_bateau        [ Add a boat ]                                                         |
                |                                                                                                       |
                |           vider_cases_jouees   [ Empty players box ]                                                  |
                |                                                                                                       |
                |           obtenir_case_bateau  [ Return boat box ]                                                    |    
                |                                                                                                       |    
                |           obtenir_pseudonyme   [ Return pseudo of player ]                                            |
                |                                                                                                       |                               
                |           obtenir_cases_jouees [ Return players box place ]                                           |
                --------------------------------------------------------------------------------------------------------

    grille :    --------------------------------------------------------------------------------------------------------
                |  Grille -> __init__ [ Initialize the game grids ]                                                     |
                |                                                                                                       |
                |            __creer_grille  [ Create the game squares ]                                                |
                |                                                                                                       |
                |            vider_grille    [ Make all the boxes empty ]                                               |
                |                                                                                                       |
                |            obtenir_grille  [ Return the grid ]                                                        |
                |                                                                                                       |
                |            obtenir_case    [ Return the boxes ]                                                       |
                |                                                                                                       |
                |            obtenir_case_aleatoire  [ Return the random boxes ]                                        |
                |                                                                                                       |    
                |            supprimer_grille  [ Remove the grid ]                                                      |
                --------------------------------------------------------------------------------------------------------

    fenetre :   --------------------------------------------------------------------------------------------------------
                |  DemandeJoueur ->  __init__ [ Initialize Tkinter ]                                                    |
                |                                                                                                       |
                |                    __creer_fenetre                                                                    |
                |                                                                                                       |
                |                    __valider_pseudonyme                                                               |
                |                                                                                                       |
                |                    changer_titre_fenetre                                                              |
                |                                                                                                       |
                |                    obtenir_bouton_valider                                                             |
                |                                                                                                       |
                |                    obtenir_etat_bouton_valider                                                        |        
                |                                                                                                       |     
                |                    obtenir_joueurs                                                                    |        
                |                                                                                                       |            
                |                    supprimer_fenetre                                                                  |    
                |                                                                                                       |     
                |                                                                                                       |
                |  AfficherGrille -> __init__                                                                           |         
                |                                                                                                       |
                |                    __creer_fenetre                                                                    |    
                |                                                                                                       |
                |                    __cliquer_fenetre                                                                  |    
                |                                                                                                       |
                |                    __valider_tour                                                                     |    
                |                                                                                                       |
                |                    obtenir_grille                                                                     |    
                |                                                                                                       |    
                |                    obtenir_bouton_valider                                                             |
                |                                                                                                       |
                |                    obtenir_etat_bouton_valider                                                        |    
                |                                                                                                       |    
                |                    vider_grille                                                                       |
                |                                                                                                       |    
                |                    obtenir_cases_selectionnees                                                        |
                |                                                                                                       |
                |                    changer_message_info                                                               |    
                |                                                                                                       |
                |                    changer_texte_bouton_valider                                                       |
                |                                                                                                       |
                |                    supprimer_fenetre                                                                  |                                                                            
                |                                                                                                       |
                |                    changer_selection                                                                  |
                --------------------------------------------------------------------------------------------------------

    case :      --------------------------------------------------------------------------------------------------------
                |  Etat -> {use Enum setting} [ say if a box is available or not ]                                      |
                |                                                                                                       |
                |  Case -> __init__  [ Link states to boxes ]                                                           |
                |                                                                                                       |
                |          changer_etat                                                                                 |
                |                                                                                                       |
                |          obtenir_etat_case                                                                            |
                |                                                                                                       |
                |          obtenir_case                                                                                 |
                |                                                                                                       |
                |          obtenir_x                                                                                    |
                |                                                                                                       |    
                |          obtenir_y                                                                                    |
                --------------------------------------------------------------------------------------------------------
"""



""" IMPORT """

from tkinter import *
from enum import Enum
import random

""" IMPORT """

"""   -------- case --------   """

class Etat(Enum):
    DISPONIBLE = 0
    INDISPONIBLE = 1
    SELECTIONNEE = 2
    DECOUVERTE = 3

class Case(object):

    def __init__(self, f: Tk, x: int, y: int):
        self.__f = f
        self.__x = x
        self.__y = y
        self.__etat = Etat.DISPONIBLE

        self.__case = Button(f)
        self.__case.place(x=x * 50, y=y * 50, width=50, height=50)

    def changer_etat(self, etat: int):
        self.__etat = etat

        if self.__etat == Etat.DISPONIBLE:
            self.__case.configure(bg='#d9d9d9')
        elif self.__etat == Etat.SELECTIONNEE:
            self.__case.configure(bg='#ffffff')
        elif self.__etat == Etat.INDISPONIBLE:
            self.__case.configure(bg='#919191')
        else:
            self.__case.configure(bg='#008f0e')

    def obtenir_etat_case(self) -> int:
        return self.__etat

    def obtenir_case(self) -> Button:
        return self.__case

    def obtenir_x(self) -> int:
        return self.__x

    def obtenir_y(self) -> int:
        return self.__y

"""   -------- case --------   """

"""   -------- joueur --------   """

class Joueur(object):

    def __init__(self, pseudonyme: str):
        self.__pseudonyme = pseudonyme
        self.__cases_jouees = []

    def ajouter_case_jouee(self, case: Case):
        self.__cases_jouees.append(case)

    def retirer_case_jouee(self, case: Case):
        self.__cases_jouees.remove(case)

    def placer_bateau(self, case: Case):
        self.__bateau = case

    def vider_cases_jouees(self):
        self.__cases_jouees = []

    def obtenir_case_bateau(self) -> Case:
        return self.__bateau

    def obtenir_pseudonyme(self) -> str:
        return self.__pseudonyme

    def obtenir_cases_jouees(self) -> list:
        return self.__cases_jouees

"""   -------- joueur --------   """

"""   -------- grille --------   """


class Grille(object):

    def __init__(self, f: Tk, largeur: int, hauteur: int):
        self.__f = f
        self.__largeur = largeur
        self.__hauteur = hauteur

        self.__creer_grille()

    def __creer_grille(self):
        print("Création d'une grille de taille " + str(self.__largeur) + "x" + str(self.__hauteur))

        self.__grille = []

        for x in range(self.__largeur):
            self.__grille.append([])
            for y in range(self.__hauteur):
                self.__grille[x].append([])
                self.__grille[x][y] = Case(self.__f, x, y)

    def vider_grille(self):
        for x in range(self.__largeur):
            for y in range(self.__hauteur):
                self.__grille[x][y].changer_etat(Etat.DISPONIBLE)

    def obtenir_grille(self) -> list:
        return self.__grille

    def obtenir_case(self, x, y) -> Case:
        return self.__grille[x][y]

    def obtenir_case_aleatoire(self) -> Case:
        return self.__grille[random.randint(0, self.__largeur) - 1][random.randint(0, self.__hauteur) - 1]

    def supprimer_grille(self):
        for x in range(self.__largeur):
            for y in range(self.__hauteur):
                self.__grille[x][y].obtenir_case().destroy()

"""   -------- grille --------   """

"""   -------- fenetre --------   """

class DemandeJoueur(object):

    def __init__(self, f: Tk):
        self.__f = f
        self.__joueurs = []

        self.__creer_fenetre()

    def __creer_fenetre(self):
        self.__f.minsize(width=250, height=80)
        self.__f.maxsize(width=250, height=80)

        self.__titre_texte = StringVar()
        self.__titre = Label(self.__f, textvariable=self.__titre_texte, relief=RAISED)
        self.__titre.place(x=10, y=5, width=230, height=20)
        self.__titre_texte.set("Bataille Navale")

        self.__entree_pseudonyme = Entry(self.__f)
        self.__entree_pseudonyme.place(x=20, y=30, width=210, height=20)

        self.__etat_bouton_valider = IntVar()
        self.__bouton_valider = Button(self.__f, text="Valider", command=lambda: self.__valider_pseudonyme(self.__entree_pseudonyme))
        self.__bouton_valider.place(x=20, y=50, width=210, height=20)

    def __valider_pseudonyme(self, entree: Entry):
        self.__etat_bouton_valider.set(1)
        self.__joueurs.append(Joueur(entree.get()))
        entree.delete(0, "end")

    def changer_titre_fenetre(self, titre: str):
        self.__titre_texte.set(titre)

    def obtenir_bouton_valider(self) -> Button:
        return self.__bouton_valider

    def obtenir_etat_bouton_valider(self) -> IntVar:
        return self.__etat_bouton_valider

    def obtenir_joueurs(self) -> list:
        return self.__joueurs

    def supprimer_fenetre(self):
        self.__titre.destroy()
        self.__entree_pseudonyme.destroy()
        self.__bouton_valider.destroy()

class AfficherGrille(object):

    def __init__(self, f: Tk, largeur: int, hauteur: int, selection_max: int):
        self.__f = f
        self.__hauteur_grille = largeur
        self.__largeur_grille = hauteur
        self.__selection_max = selection_max
        self.__selection = 0

        self.__creer_fenetre()

    def __creer_fenetre(self):
        self.__f.minsize(width=50 * self.__largeur_grille, height=50 * self.__hauteur_grille)
        self.__f.maxsize(width=50 * self.__largeur_grille, height=60 * self.__hauteur_grille)

        self.__canvas = Canvas(self.__f, width=50 * self.__largeur_grille, height=50 * self.__hauteur_grille, bg='white')
        self.__canvas.pack()

        self.__info_texte = StringVar()
        self.__info = Label(self.__f, textvariable=self.__info_texte, relief=SUNKEN)
        self.__info.pack()
        self.__info_texte.set(" Au tour de Roger ")

        self.__grille = Grille(self.__f, self.__largeur_grille, self.__hauteur_grille)

        self.__f.bind("<1>", self.__cliquer_fenetre)

        self.__etat_bouton_valider = IntVar()
        self.__bouton_valider_texte = StringVar()
        self.__bouton_valider = Button(self.__f, textvariable=self.__bouton_valider_texte, command=lambda: self.__valider_tour())

    def __cliquer_fenetre(self, event):
        for x in range(self.__largeur_grille):
            for y in range(self.__hauteur_grille):
                case = self.__grille.obtenir_case(x, y)
                if case.obtenir_case() == event.widget:
                    if case.obtenir_etat_case() == Etat.DISPONIBLE:
                        if self.__selection < self.__selection_max:
                            self.__selection += 1
                            case.changer_etat(Etat.SELECTIONNEE)
                    elif case.obtenir_etat_case() == Etat.SELECTIONNEE:
                        self.__selection -= 1
                        case.changer_etat(Etat.DISPONIBLE)
        if self.__selection == self.__selection_max:
            self.__bouton_valider.pack() 
        else:
            self.__bouton_valider.pack_forget() 

    def __valider_tour(self):
        self.__etat_bouton_valider.set(1)

    def obtenir_grille(self) -> Grille:
        return self.__grille

    def obtenir_bouton_valider(self) -> Button:
        return self.__bouton_valider

    def obtenir_etat_bouton_valider(self) -> IntVar:
        return self.__etat_bouton_valider

    def vider_grille(self):
        self.__grille.vider_grille()
        self.__selection = 0

    def obtenir_cases_selectionnees(self) -> list:
        cases = []
        for x in range(self.__largeur_grille):
            for y in range(self.__hauteur_grille):
                case = self.__grille.obtenir_case(x, y)
                if case.obtenir_etat_case() == Etat.SELECTIONNEE:
                    cases.append(case)
        return cases

    def changer_message_info(self, texte: str):
        self.__info_texte.set(texte)

    def changer_texte_bouton_valider(self, texte: str):
        self.__bouton_valider_texte.set(texte)

    def supprimer_fenetre(self):
        self.__canvas.destroy()
        self.__info.destroy()
        self.__grille.supprimer_grille()
        self.__bouton_valider.destroy()
        self.__f.unbind("<1>")

    def changer_selection(self, selection: int):
        self.__selection = selection

"""   -------- fenetre --------   """

"""   -------- main --------   """

class Bataille(object):

    def __init__(self):
        self.__f = Tk()
        self.__f.title("Bataille Navale 5x5")
        self.__f.resizable(False, False)

        self.__joueurs = self.__demander_joueurs()
        self.__lancer_partie()

    def __demander_joueurs(self) -> Joueur:
        fenetre_pseudo = DemandeJoueur(self.__f)
        for i in range(2):
            fenetre_pseudo.changer_titre_fenetre(" Entrez le pseudonyme du joueur " + str(i) + ": ")
            fenetre_pseudo.obtenir_bouton_valider().wait_variable(fenetre_pseudo.obtenir_etat_bouton_valider())
        fenetre_pseudo.supprimer_fenetre()
        return fenetre_pseudo.obtenir_joueurs()

    def __placer_bateaux(self, joueurs: list):
        for joueur in joueurs:
            joueur.placer_bateau(self.__grille.obtenir_case_aleatoire())

    def __lancer_partie(self):
        fenetre_grille = AfficherGrille(self.__f, 5, 5, 3)
        self.__grille = fenetre_grille.obtenir_grille()

        joueurs_aleatoires = random.sample(self.__joueurs, 2)
        fenetre_grille.changer_message_info(joueurs_aleatoires[0].obtenir_pseudonyme() + " joue contre " + joueurs_aleatoires[1].obtenir_pseudonyme())
        fenetre_grille.changer_texte_bouton_valider("Commencer")
        fenetre_grille.obtenir_bouton_valider().pack()
        fenetre_grille.changer_selection(3)
        fenetre_grille.obtenir_bouton_valider().wait_variable(fenetre_grille.obtenir_etat_bouton_valider())
        fenetre_grille.changer_selection(0)
        self.__placer_bateaux(joueurs_aleatoires)
        tour = 0
        jouer = True

        while jouer:
            if (tour % 2) == 0:
                joueur = joueurs_aleatoires[0]
                adversaire = joueurs_aleatoires[1]
                fenetre_grille.changer_message_info("Au tour de " + joueurs_aleatoires[0].obtenir_pseudonyme())
            else:
                joueur = joueurs_aleatoires[1]
                adversaire = joueurs_aleatoires[0]
                fenetre_grille.changer_message_info("Au tour de " + joueurs_aleatoires[1].obtenir_pseudonyme())
            fenetre_grille.changer_texte_bouton_valider("Valider")
            fenetre_grille.vider_grille()
            fenetre_grille.obtenir_bouton_valider().pack_forget()

            for case in joueur.obtenir_cases_jouees():
                fenetre_grille.obtenir_grille().obtenir_case(case.obtenir_x(), case.obtenir_y()).changer_etat(Etat.INDISPONIBLE)

            fenetre_grille.obtenir_bouton_valider().wait_variable(fenetre_grille.obtenir_etat_bouton_valider())

            for case in fenetre_grille.obtenir_cases_selectionnees():
                fenetre_grille.obtenir_grille().obtenir_case(case.obtenir_x(), case.obtenir_y()).changer_etat(Etat.INDISPONIBLE)
                joueur.ajouter_case_jouee(case)
                if adversaire.obtenir_case_bateau() == case:
                    fenetre_grille.changer_message_info("Victoire de " + joueur.obtenir_pseudonyme())
                    case.changer_etat(Etat.DECOUVERTE)
                    fenetre_grille.changer_texte_bouton_valider("Continuer le tournoi")
                    fenetre_grille.obtenir_bouton_valider().wait_variable(fenetre_grille.obtenir_etat_bouton_valider())
                    joueur.vider_cases_jouees()
                    
                    self.__joueurs.remove(adversaire)
                    
                    jouer = False
                    break


            tour += 1
        if len(self.__joueurs) == 1:
            fenetre_grille.changer_message_info(self.__joueurs[0].obtenir_pseudonyme() + " remporte le tournoi!")
            fenetre_grille.changer_texte_bouton_valider("Recommencer")
            fenetre_grille.obtenir_bouton_valider().wait_variable(fenetre_grille.obtenir_etat_bouton_valider())
            fenetre_grille.supprimer_fenetre()
            self.__joueurs = self.__demander_joueurs()
            self.__lancer_partie()
        else:
            fenetre_grille.supprimer_fenetre()
            self.__lancer_partie()

    def demarrer(self):
        self.__f.mainloop()


"""   -------- main --------   """


main = Bataille()
main.demarrer()
