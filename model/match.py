"""
fichier ayant la classe match qui corespond à un match
pour chaque match on conservera le
score des deux joueurs, le vainqueur a un score de 1 point
le perdant on score de 0
en cas de match nul chaqu'un a 1/2 point
"""
import datetime
class Match():
    """un match est composé de deux listes la premi-re contient le nom des
     deux joueurs et le second leur scores respectifs à l'issue du match"""
    def __init__(self, player1, player2,player1_score=0,player2_score=0):
        self.player_list = [player1,player2]
        self.score_list = [player1_score,player2_score]



class Round():
    """un round ou un tour est constitué de la liste des matchs le constituants et des dates
    de debut et fin"""
    def __init__(self,list_of_match):
        self.list_of_match = list_of_match
        self.begin_date = datetime.datetime.now()
        self.end_date = None


class Tournament():
    """un tournoi est defini par un nom, le lieu où se déroule le tournoi, le nombre de round par défaut égal
    à 4 de la liste des rounds, de listes des joueurs, d'un control de temps et une description du
    directeur du tounoir"""
    def __init__(self,name,place,description,number_of_round=4,list_of_round=[],
                 list_of_player=[]):
        self.name = name
        self.place = place
        self.date = datetime.datetime.now()
        self.number_of_round = number_of_round
        self.list_of_round = list_of_round
        self.list_of_player = list_of_player
        self.description = description


