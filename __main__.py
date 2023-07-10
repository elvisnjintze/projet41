"""
ficher principal permettant de lancer l'application:
"""

from controler.controler import Controler
from view import view


v = view.View()
c = Controler(v)
c.run()
