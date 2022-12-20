import pygame as p
from math import floor
from settings import *
from sys import stdout

class GUI:
    def __init__(self, __board):
        p.init()
        self.screen = p.display.set_mode((GUI_BOARD_WIDTH, GUI_BOARD_HEIGHT+2*GUI_GRAVEYARD_HEIGHT))
        self.clock = p.time.Clock()
        stdout.flush()
        self.piece_images = {}
        self.loadImages()
        self.board = __board
        
        self.sqSelected = () #holds coord of last click of user (tuple: row, col)
        self.playerClicks = [] #list that keep track of player clicks (2 tuples[(6, 4), (4, 4)]

        self.highlighted_tiles = []


    def loadImages(self):
        pieces = ['p', 'r', 'n', 'b', 'q', 'k', 'P', 'R', 'N', 'B', 'Q', 'K']
        for piece in pieces:
            self.piece_images[piece] = p.transform.scale(p.image.load(PIECE_IMG_MAPPING[piece]), (GUI_SQ_SIZE, GUI_SQ_SIZE))

    def drawLines(self):
        color = p.Color("black")
        for row in range(1,BOARD_DIM):
            for col in range(1,BOARD_DIM):
                p.draw.line(self.screen, color, (col*GUI_SQ_SIZE, GUI_GRAVEYARD_HEIGHT), (col*GUI_SQ_SIZE, GUI_BOARD_WIDTH+GUI_GRAVEYARD_HEIGHT), 2)
                #separate rows
                p.draw.line(self.screen, color, (0, GUI_GRAVEYARD_HEIGHT+row*GUI_SQ_SIZE), (GUI_BOARD_HEIGHT, GUI_GRAVEYARD_HEIGHT+row*GUI_SQ_SIZE), 2)

    def drawLettersNumbers(self):
        for row in range(0,BOARD_DIM):
            font = p.font.SysFont(None, 20)
            text = font.render(str(abs(row-8)), True, p.Color("black"))
            self.screen.blit(text, (0, GUI_GRAVEYARD_HEIGHT+row*GUI_SQ_SIZE+5))
        
        for col in range(0,BOARD_DIM):
            font = p.font.SysFont(None, 20)
            text = font.render(FILE_INT_TO_STR_MAPPING[col], True, p.Color("black"))
            self.screen.blit(text, (col*GUI_SQ_SIZE+2, GUI_GRAVEYARD_HEIGHT+BOARD_DIM*GUI_SQ_SIZE-15))
    
    def drawHighlightMoves(self):
        color = p.Color(BOARD_COLOR_HIGHLIGHTED_TILES)
        for move in self.highlighted_tiles:
            p.draw.rect(self.screen, color, p.Rect(FILE_STR_TO_INT_MAPPING[move[0]]*GUI_SQ_SIZE, GUI_GRAVEYARD_HEIGHT+(8-int(move[1]))*GUI_SQ_SIZE, GUI_SQ_SIZE, GUI_SQ_SIZE))
				

    def drawSquares(self):
        colors = [p.Color(BOARD_COLOR_1), p.Color(BOARD_COLOR_2)]
        for row in range(BOARD_DIM):
            for col in range(BOARD_DIM):
                color = colors[((col+row)%2)]
                p.draw.rect(self.screen, color, p.Rect(col*GUI_SQ_SIZE, GUI_GRAVEYARD_HEIGHT+row*GUI_SQ_SIZE, GUI_SQ_SIZE, GUI_SQ_SIZE))
	
    def drawPieces(self):
        for i in range(TOTAL_SQUARES):
            rank = floor(i / 8)
            file = i % 8
            piece = self.board.piece_at(i)
            if piece != None:
                self.screen.blit(self.piece_images[str(piece)], p.Rect(file*GUI_SQ_SIZE, GUI_GRAVEYARD_HEIGHT+rank*GUI_SQ_SIZE, GUI_SQ_SIZE, GUI_SQ_SIZE))     

    def showBoard(self):
        for e in p.event.get():
            if e.type == p.QUIT:
                return False
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos() # (x, y) location of mouse
                file_int = location[0]//GUI_SQ_SIZE
                file_str = FILE_INT_TO_STR_MAPPING[file_int]
                rank_int = (location[1]-GUI_GRAVEYARD_HEIGHT)//GUI_SQ_SIZE
                rank_str = str(8-rank_int)
                tile_name = file_str + rank_str
                if self.sqSelected == tile_name: #click same square twice
                    self.sqSelected = None
                    self.playerClicks = []
                    self.highlighted_tiles = []
                else: #clicked a new square
                    self.highlighted_tiles = []
                    self.sqSelected = tile_name
                    self.playerClicks.append(self.sqSelected)
                    print(self.playerClicks)
                    for move in self.board.legal_moves:
                        from_tile = str(move)[0] + str(move)[1]
                        if (self.sqSelected == from_tile):
                            self.highlighted_tiles.append(str(move)[2] + str(move)[3])

                # if len(self.playerClicks) == 2:
                #     print("Make Move")
                #     self.playerClicks = []
					
        self.drawSquares()
        self.drawHighlightMoves()
        self.drawLines()
        self.drawLettersNumbers()
        self.drawPieces()
        self.clock.tick(FPS)
        p.display.flip()

        return True