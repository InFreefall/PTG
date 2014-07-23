import pygame
import crashReporter
from pygame.locals import *
import sys

from battle import Battle

def main():
    crashReporter.install_execpthook()
    pygame.init()
    battle = Battle()
    try:
        battle.run()
    finally:
        battle.client.disconnect()
