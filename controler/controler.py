"""ceci est le fichier controleur qui contient la classe
 Controleur qui l'aiguilleur de notre application
nous commencons par le constructeur qui doit instancier tous les models
et les vues dont il aura besoin"""
from model import match
from model import player
from view import view
from tinydb import TinyDB


class Controler():
    def __init__(self, view):
        self.player = []
        self.view = view
        self.round_list = []
        self.round1 = []
        self.tour = None
        self.list_of_match_play = []

    def create_tournament(self):
        """méthode permettant de créer un tournoi"""
        # le nom du tournoi
        name_tournament = self.view.ask_name_tournament()
        # le lieu ou de déroule le tournoi
        place_tournament = self.view.ask_place_tournament()
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
        #on rafléchit la liste des match joué
        self.list_of_match_play = self.round1
        self.tour = match.Tournament(name=name_tournament,place=place_tournament,
                                     description=description_tournament,list_of_round=[],
                                     list_of_player=self.player)

    def sort_player_by_point(self):
        """cete fonction permet de trier la liste nomée player des joueurs selon leurs points cumulés
        si deux joueurs ont le meme nombre de point alors ils sont triés en fonction de leur classement"""
        i = 0
        while len(self.player)>i:
            plus_grand = self.player[i].point
            j = i+1
            while j<len(self.player):
                if self.player[j].point>plus_grand:
                    plus_grand = self.player[j].point
                    b = self.player[i]
                    self.player[i] = self.player[j]
                    self.player[j] = b
                j = j+1
            i = i+1

    def verify_match(self,match):
        """cette fonction prend en paramètre un match et verifie si ce match a déjà été joué
        dans la liste de match dejà joués list_of_match_play et retourne TRUE si oui et FALSE sinon"""
        for i in self.list_of_match_play:
            if (i.player_list[0].family_name==match.player_list[0].family_name and i.player_list[1].family_name==match.player_list[1].family_name):
                return True
            if (i.player_list[0].family_name==match.player_list[1].family_name and i.player_list[1].family_name==match.player_list[0].family_name):
                return True
        return False


    def generate_next_round(self):
        """cette fonction permet de générer un nouveau round avec une politique de génération différent du premier
        round ici on tient plutot des point ou du cummul des scores"""
        i = 0
        self.round1 = []
        while i<len(self.player)-1:
            #on crée un match qu'on doit affecter au round actuel
            m = match.Match(self.player[i],self.player[i+1])
            i = i+2
            #il faut controler si ce match existe dans la liste des match deja joués "list_of_match_play"
            #on appele la fontion verify_match avec en paramètr m
            if not self.verify_match(m):
                self.round1.append(m)
        self.list_of_match_play = self.list_of_match_play + self.round1
        self.round_list.append(self.round1)
        print(len(self.list_of_match_play))

    def type_result(self):
        """on recupère le score de chaque joueur à partir du round 2 à 4 qu'on met dans dans l'objet Match
        de la liste round1 ensuit on increment l'attribut point de chaque joueur
        avec son score lors de ce match"""
        j = 0
        for i in self.round1:
            #print(i.player_list[0].family_name)
            result = self.view.ask_result(i.player_list[0].family_name,i.player_list[1].family_name)
            i.score_list = result
            #on doit parcourir la    liste player et trouver chaque joueur et incremente son nombre de point
            find = False
            j = 0
            while not find and len(self.player)>=j:
                if i.player_list[0].family_name == self.player[j].family_name:
                    self.player[j].point = self.player[j].point + result[0]
                    find = True
                j = j+1
            find = False
            j= 0
            while not find and len(self.player)>=j:
                if i.player_list[1].family_name == self.player[j].family_name:
                    self.player[j].point = self.player[j].point + result[1]
                    find = True
                j = j+1

    def serialisation_player(self):
        liste = []
        for i in self.player:
            serial = {'family name': i.family_name,
                      'second name': i.second_name,
                     'birthday': i.birthday,
                      'sex': i.sex,
                      'classement': i.classement,
                      'point': i.point}
            liste.append(serial)
        #on crée et insere la liste dans une DB et à la table player
        db = TinyDB('db.json')
        players_table = db.table('players')
        players_table.truncate()  # clear the table first
        players_table.insert_multiple(liste)

    def serialisation_tounament(self):
        #on extrait la liste des matchs
        liste_des_matchs = []
        for i in self.list_of_match_play:
            name1 = i.player_list[0].family_name
            name2 = i.player_list[1].family_name
            m = (name1,name2)
            liste_des_matchs.append(m)
        serial = {'nom du tournois':self.tour.name,
                  'lieu du tournois':self.tour.place,
                  'date du tournois':str(self.tour.date),
                  'nombre de rounds du tournois':self.tour.number_of_round,
                  'description du tournois':self.tour.description,
                  'liste des matchs joués pendant le tournois':liste_des_matchs }
        db = TinyDB('db.json')
        tournois_table = db.table('tournament')
        tournois_table.truncate()  # clear the table first
        tournois_table.insert(serial)


    def show_state(self):
        """ méthode pour afficher les différentes informations sur le tournoi"""
        if self.view.ask_state()=="1":
            db = TinyDB('db.json')
            bd = db.all()
            self.view.show_infos(bd)
        self.view.show_infos("merci d'etre passé. ce fut une expérience remarquable. A une autre fois")


    def run(self):
        """méthode permettant d'exècuter le programme
        premierement on crée un tournoi"""
        self.create_tournament()
        #on doit entrer le score de chaque pour chaque match
        self.type_result()
        for i in range(match.NOMBRES_DE_TOURS-1):
            #on ordonne la liste des joueurs
            self.sort_player_by_point()
            #on genere un nouveau round
            self.generate_next_round()
            self.type_result()
        #une fois terminer, on passe à la sérialisation
        self.sort_player_by_point()
        self.serialisation_player()
        self.tour.list_of_round = self.round_list
        self.serialisation_tounament()
        #self.show_state()

