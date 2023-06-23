"""
ce fichier contient les informations sur les jioueurs
"""

class Joueur():
    """"classe représentant un joueur"""
    def __init__(self,name,second_name,birthday,sex,classement=None):
        self.family_name = name
        self.second_name = second_name
        self.birthday = birthday
        self.sex = sex
        self.clasement = classement
        self.point = 0