import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.Load_Save import GameData
from Principal.Main_Menu import MenuState

class BatalhaMenu(MenuState):

    def execute(self):
        print("Menu de batalha")
