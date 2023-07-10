"""fichier contenant la vue de tout ce qui sera affiché à l'utilisateur"""
class View():
    """classe permettant la collecte de l'information sur les joueurs"""
    def ask_list_of_player_tournament(self):
        """fction permetant de demander les noms des huit joueurs"""
        liste_joueur = []
        for i in range(8):
            name = input(f"entrez le nom du joueur numeros {i+1}: ")
            second_name = input(f"entrez le prenom du joueur  {name}: ")
            birthday = input(f"entrez la date de naissance du joueur  {name} {second_name}: ")
            sex = input(f"entrez le sex du joueur  {name} {second_name}: ")
            joueur = {"name":name,"second_name":second_name,"birthday":birthday,"sex":sex}
            liste_joueur.append(joueur)
        return liste_joueur

    def ask_name_tournament(self):
        """nom du tournoi"""
        return input("entrez le nom du tournoi: ")

    def ask_place_tournament(self):
        """lieu où se déroule le tournoi"""
        return input("entrez le lieu où se déroule ce tournoi: ")

    def ask_description_tournament(self):
        """fction qui permet de demander la description du tournoi"""
        return input("quelle est la description du tournoi: ")

    def show_infos(self,infos):
        print(infos)

    def ask_state(self):
        s = input("désirez vous afficher les informations liées au déroulement du tournoi, si oui tapez 1 ou tout autre sinon.")
        return s

    def ask_result(self,joueur1,joueur2):
        """fction qui prend en paramètre les noms de deux joueurs: joueur1 et joueur2 et
         permet d'entrer les scores pour les deux joueurs après leur match et retourne une liste
         de deux élts [score_du_joueur1,score_du_joueur2]"""
        s1 = input(f"entrez le score du joueur {joueur1} lors du match qui l'a opposé à  {joueur2}: ")
        s2 = input(f"entrez le score du joueur {joueur2} lors du match qui l'a opposé à  {joueur1}: ")
        try:
            s = [float(s1.replace(',','.')),float(s2.replace(',','.'))]
            return s
        except ValueError:
            print("vous n'aves pas entrez des scores à valeur réel exemple 0.5")

