import pygame as p
from math import floor
from settings import *
from sys import stdout

class GUI:
    def __init__(self, __board):
        p.init()
        self.screen = p.display.set_mode((GUI_WIDTH, GUI_HEIGHT))
        self.clock = p.time.Clock()
        stdout.flush()
        self.piece_images = {}
        self.loadImages()
        self.board = __board

    def loadImages(self):
        imgPath = "png\\"
        pieceMapping = {
            "b": imgPath + "b.png",
            "k": imgPath + "k.png",
            "n": imgPath + "n.png",
            "p": imgPath + "p.png",
            "q": imgPath + "q.png",
            "r": imgPath + "r.png",
            "B": imgPath + "Bb.png",
            "K": imgPath + "Bk.png",
            "N": imgPath + "Bn.png",
            "P": imgPath + "Bp.png",
            "Q": imgPath + "Bq.png",
            "R": imgPath + "Br.png",
        }
        pieces = ['p', 'r', 'n', 'b', 'q', 'k', 'P', 'R', 'N', 'B', 'Q', 'K']
        for piece in pieces:
            self.piece_images[piece] = p.transform.scale(p.image.load(pieceMapping[piece]), (GUI_SQ_SIZE, GUI_SQ_SIZE))

    
    def drawSquares(self):
        colors = [p.Color(BOARD_COLOR_1), p.Color(BOARD_COLOR_2)]
        for row in range(BOARD_DIM):
            for col in range(BOARD_DIM):
                color = colors[((col+row)%2)]
                p.draw.rect(self.screen, color, p.Rect(col*GUI_SQ_SIZE, row*GUI_SQ_SIZE, GUI_SQ_SIZE, GUI_SQ_SIZE))
	
    def drawPieces(self):
        for i in range(TOTAL_SQUARES):
            rank = floor(i / 8)
            file = i % 8
            piece = self.board.piece_at(i)
            if piece != None:
                self.screen.blit(self.piece_images[str(piece)], p.Rect(file*GUI_SQ_SIZE, rank*GUI_SQ_SIZE, GUI_SQ_SIZE, GUI_SQ_SIZE))     

    def showBoard(self):
        running = True
        while running:
            for e in p.event.get():
                if e.type == p.QUIT:
                    running = False
            self.drawSquares()
            self.drawPieces()
            self.clock.tick(FPS)
            p.display.flip()