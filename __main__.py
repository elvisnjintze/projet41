"""
fichier de lancement de l'application
"""
from view import view
from controler.controler import Controler

v = view.View()
c = Controler(v)
c.run()
