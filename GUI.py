import pygame as p
from math import floor
from settings import *
from sys import stdout

class GUI:
    def __init__(self, __board):
        p.init()
        width = GUI_BOARD_WIDTH+GUI_SPACING_COLUMN_WIDTH*2+GUI_SIDEBAR_WIDTH
        height = GUI_BOARD_HEIGHT+2*GUI_GRAVEYARD_HEIGHT
        self.screen = p.display.set_mode((width, height))
        self.clock = p.time.Clock()
        stdout.flush()
        self.piece_images = {}
        self.loadImages()
        self.board = __board
        
        self.sq_selected = () #holds coord of last click of user (tuple: row, col)
        self.player_clicks = [] #list that keep track of player clicks (2 tuples[(6, 4), (4, 4)]

        self.highlighted_tiles = []


    def loadImages(self):
        pieces = ['p', 'r', 'n', 'b', 'q', 'k', 'P', 'R', 'N', 'B', 'Q', 'K']
        for piece in pieces:
            self.piece_images[piece] = p.transform.scale(p.image.load(PIECE_IMG_MAPPING[piece]), (GUI_SQ_SIZE, GUI_SQ_SIZE))

    def drawLines(self):
        color = p.Color("black")
        for row in range(1,BOARD_DIM):
            for col in range(1,BOARD_DIM):
                #separate cols
                x_start = GUI_SPACING_COLUMN_WIDTH+col*GUI_SQ_SIZE
                x_end = GUI_SPACING_COLUMN_WIDTH+col*GUI_SQ_SIZE
                y_start = GUI_GRAVEYARD_HEIGHT
                y_end = GUI_BOARD_WIDTH+GUI_GRAVEYARD_HEIGHT
                p.draw.line(self.screen, color, (x_start, y_start), (x_end, y_end), 2)
                #separate rows
                x_start = GUI_SPACING_COLUMN_WIDTH
                x_end = GUI_SPACING_COLUMN_WIDTH+GUI_BOARD_HEIGHT
                y_start = GUI_GRAVEYARD_HEIGHT+row*GUI_SQ_SIZE
                y_end = GUI_GRAVEYARD_HEIGHT+row*GUI_SQ_SIZE
                p.draw.line(self.screen, color, (x_start, y_start), (x_end, y_end), 2)

    def drawLettersNumbers(self):
        for row in range(0,BOARD_DIM):
            font = p.font.SysFont(None, 20)
            text = font.render(str(abs(row-8)), True, p.Color("black"))
            x_pos = GUI_SPACING_COLUMN_WIDTH
            y_pos = GUI_GRAVEYARD_HEIGHT+row*GUI_SQ_SIZE+5
            self.screen.blit(text, (x_pos, y_pos))
        
        for col in range(0,BOARD_DIM):
            font = p.font.SysFont(None, 20)
            text = font.render(FILE_INT_TO_STR_MAPPING[col], True, p.Color("black"))
            x_pos = GUI_SPACING_COLUMN_WIDTH+col*GUI_SQ_SIZE+2
            y_pos = GUI_GRAVEYARD_HEIGHT+BOARD_DIM*GUI_SQ_SIZE-15
            self.screen.blit(text, (x_pos, y_pos))
    
    def drawHighlightMoves(self):
        color = p.Color(BOARD_COLOR_HIGHLIGHTED_TILES)
        for move in self.highlighted_tiles:
            left_pos = GUI_SPACING_COLUMN_WIDTH+FILE_STR_TO_INT_MAPPING[move[0]]*GUI_SQ_SIZE
            top_pos = GUI_GRAVEYARD_HEIGHT+(8-int(move[1]))*GUI_SQ_SIZE
            p.draw.rect(self.screen, color, p.Rect(left_pos, top_pos, GUI_SQ_SIZE, GUI_SQ_SIZE))
				

    def drawSquares(self):
        colors = [p.Color(BOARD_COLOR_1), p.Color(BOARD_COLOR_2)]
        for row in range(BOARD_DIM):
            for col in range(BOARD_DIM):
                color = colors[((col+row)%2)]
                left_pos = GUI_SPACING_COLUMN_WIDTH+col*GUI_SQ_SIZE
                top_pos = GUI_GRAVEYARD_HEIGHT+row*GUI_SQ_SIZE
                p.draw.rect(self.screen, color, p.Rect(left_pos, top_pos, GUI_SQ_SIZE, GUI_SQ_SIZE))
	
    def drawPieces(self):
        for i in range(TOTAL_SQUARES):
            rank = floor(i / 8)
            file = i % 8
            piece = self.board.piece_at(i)
            if piece != None:
                left_pos = GUI_SPACING_COLUMN_WIDTH+file*GUI_SQ_SIZE
                top_pos = GUI_GRAVEYARD_HEIGHT+rank*GUI_SQ_SIZE
                self.screen.blit(self.piece_images[str(piece)], p.Rect(left_pos, top_pos, GUI_SQ_SIZE, GUI_SQ_SIZE))     

    def showBoard(self):
        for e in p.event.get():
            if e.type == p.QUIT:
                return False
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos() # (x, y) location of mouse
                x_mouse = location[0]
                y_mouse = location[1]
                if(x_mouse > GUI_BOARD_WIDTH_OFFSET and x_mouse < GUI_BOARD_WIDTH + GUI_BOARD_WIDTH_OFFSET) and (y_mouse > GUI_BOARD_HEIGHT_OFFSET and y_mouse < GUI_BOARD_HEIGHT + GUI_BOARD_HEIGHT_OFFSET):
                    file_int = (location[0]-GUI_BOARD_WIDTH_OFFSET)//GUI_SQ_SIZE
                    file_str = FILE_INT_TO_STR_MAPPING[file_int]
                    rank_int = (location[1]-GUI_BOARD_HEIGHT_OFFSET)//GUI_SQ_SIZE
                    rank_str = str(8-rank_int)
                    tile_name = file_str + rank_str
                    if self.sq_selected == tile_name: #click same square twice
                        self.sq_selected = None
                        self.player_clicks = []
                        self.highlighted_tiles = []
                    else: #clicked a new square
                        self.highlighted_tiles = []
                        self.sq_selected = tile_name
                        self.player_clicks.append(self.sq_selected)
                        print(f"player clicked: {self.player_clicks}")

                        found_move = False

                        if len(self.player_clicks) == 2:
                            move_str = self.player_clicks[0] + self.player_clicks[1]
                            print(move_str)
                            for move in self.board.legal_moves:
                                if move_str == str(move):
                                    print("Good Move")
                                    found_move = True
                                    self.player_clicks = []
                                    self.highlighted_tiles = []
                                    #TODO: MAKE MOVE
                            if found_move is False:
                                self.player_clicks = [self.sq_selected]
                        if len(self.player_clicks) == 1:
                            for move in self.board.legal_moves:
                                if tile_name == str(move)[0]+str(move)[1]:
                                    self.highlighted_tiles.append(str(move)[2]+str(move)[3])
                                
                                

                    
					
        self.drawSquares()
        self.drawHighlightMoves()
        self.drawLines()
        self.drawLettersNumbers()
        self.drawPieces()
        self.clock.tick(FPS)
        p.display.flip()

        return True