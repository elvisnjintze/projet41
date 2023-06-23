"""ceci est le fichier controleur qui contient la classe
 Controleur qui l'aiguilleur de notre application
nous commencons par le constructeur qui doit instancier tous les models
et les vues dont il aura besoin"""
from model import match
from model import player
from view import view

class Controler():
    def __init__(self,view):
        self.player = []
        self.view = view
        self.round_list = []
        self.round1 = []
        self.tour = None

    def create_tournament(self):
        """méthode permettant de créer un tournoi"""
        name_tournament = self.view.ask_name_tournament()#le nom du tournoi
        place_tournament = self.view.ask_place_tournament()#le lieu ou de déroule le tournoi
        #self.number_of_round = number_of_round
        #self.list_of_round = list_of_round
        # self.time_control = time_control
        description_tournament = self.view.ask_description_tournament()#description du tournoi
        list_of_player = self.view.ask_list_of_player_tournament()#liste des joueurs du tournoi
        for i in list_of_player:
            joueur = player.Joueur(name=i["name"],second_name=i["second_name"],birthday=i["birthday"],sex=i["sex"])
            self.player.append(joueur)#liste des joueurs présents dans le controleur
        #après la liste des joueurs place à la liste des round pour le premier tour
        for i in range (4):
            #on créee des paires de match pour le premier round
            m = match.Match(self.player[i],self.player[i+4])
            #chaque match est ajouté à la liste round1 donc à la fin ici on a une liste avec 4 matchs
            self.round1.append(m)
            #le round crée est ajouté à la liste des rouns
        self.round_list.append(self.round1)
        self.tour = match.Tournament(name=name_tournament,place=place_tournament,
                                     description=description_tournament,list_of_round=[],
                                     list_of_player=self.player)

    def type_result(self):
        """on recupère le score de chaque joueur qu'on met dans dans l'objet Match
        de la liste round1 ensuit on increment l'attribut point de chaque joueur
        avec son score lors de ce match"""
        j = 0
        for i in self.round1:
            #print(i.player_list[0].family_name)
            result = self.view.ask_result(i.player_list[0].family_name,i.player_list[1].family_name)
            i.score_list = result
            self.player[j].point = self.player[j].point + result[0]
            self.player[j+4].point = self.player[j+4].point + result[1]


    def run(self):
        """méthode permettant d'exècuter le programme
        premierement on crée un tournoi"""
        self.create_tournament()
        #on doit entrer le score de chaque pour chaque match
        self.type_result()


v = view.View()
c = Controler(v)
c.run()
