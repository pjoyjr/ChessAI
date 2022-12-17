import pygame as p
from settings import *

class GUI:
    def __init__(self):
        p.init()
        self.piece_images = {}
        self.loadImages()


    def loadImages(self):
        pieces = ['p', 'r', 'n', 'b', 'q', 'k', 'wp', 'wr', 'wn', 'wb', 'wq', 'wk']
        for piece in pieces:
            self.piece_images[piece] = p.transform.scale(p.image.load("png/" + piece + ".png"), (GUI_SQ_SIZE, GUI_SQ_SIZE))

