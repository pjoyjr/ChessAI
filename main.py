from engine import GameState, Move

import pygame as p  
import sys
import time

WIDTH = HEIGHT = 512
DIM = 8
SQ_SIZE = WIDTH // DIM
FPS = 18
IMAGES = {}


ONOFFAI = False # TRUE = ON, FALSE = OFF


def loadImages():
	pieces = ['bp', 'br', 'bn', 'bb', 'bq', 'bk', 'wp', 'wr', 'wn', 'wb', 'wq', 'wk']
	for piece in pieces:
		IMAGES[piece] = p.transform.scale(p.image.load("png/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))

def main():
	#setup GUI
	p.init()
	screen = p.display.set_mode((WIDTH, HEIGHT))
	clock = p.time.Clock()
	sys.stdout.flush()
	
	#Start Gamestate
	gs = GameState()
	validMoves = gs.getValidMoves()
	
	#load images for pieces
	loadImages()
	
	#flag variables
	running = True
	moveMade = False
	foundMove = False
	
	#coord variables
	sqSelected = () #holds coord of last click of user (tuple: row, col)
	playerClicks = [] #list that keep track of player clicks (2 tuples[(6, 4), (4, 4)] 
	
	while running:
		for e in p.event.get():
			if e.type == p.QUIT:
				running = False
			#mouse handler
			elif e.type == p.MOUSEBUTTONDOWN:
				location = p.mouse.get_pos() # (x, y) location of mouse
				col = location[0]//SQ_SIZE
				row = location[1]//SQ_SIZE
				
				if sqSelected == (row, col): #click same square twice
					sqSelected = ()
					playerClicks = []
				else: #clicked a new square
					sqSelected = (row, col)
					playerClicks.append(sqSelected)
	
					if len(playerClicks) == 2:
						move = Move(playerClicks[0], playerClicks[1], gs.board, 0)
						foundMove = False
						for moves in validMoves:
							if move.moveID == moves.moveID:
								gs.makeMove(moves)
								moveMade = True
								foundMove = True
								sqSelected = ()
								playerClicks = []
					if foundMove is False:
						playerClicks = [sqSelected]
						foundMove = False
					
			#key handler
			elif e.type == p.KEYDOWN:
				if e.key == p.K_z: #undo when z is pressed
					gs.undoMove()
					
					if ONOFFAI:
						gs.undoMove()
						
					moveMade = True
		
		if moveMade:
			validMoves = gs.getValidMoves()
			moveMade = False
			
			#check for CHECK/CHECKMATE/STALEMATE
			if len(validMoves) == 0:
				winner = 't'
				if gs.checkmate:
					winner = 'b' if gs.whiteMove else 'w'
					sys.stdout.write("{} wins by Checkmate!\n".format(winner))
					sys.stdout.flush()
				elif gs.stalemate:
					sys.stdout.write("Stalemate!\n")
					sys.stdout.flush()
				gs.writeResults(winner)
				del gs
				gs = GameState()
				validMoves = gs.getValidMoves()
					
			else:
				if gs.inCheck():
					sys.stdout.write("Check!\n")
					sys.stdout.flush()
		
		#AI PLAYING
		if ONOFFAI:
			if gs.whiteMove == False:
				gs.AI(validMoves)
				moveMade = True
		
		drawGame(screen, gs, sqSelected)
		clock.tick(FPS)
		p.display.flip()
		
		
def drawGame(screen, gs, attackPiece):
	drawSquares(screen) #draw squares on board
	if len(gs.moveLog) != 0:
		drawLastMove(screen, gs)
	drawHighlightMoves(screen, gs, attackPiece)
	drawLines(screen)
	drawPieces(screen, gs.board) #draw pieces on top of squares
	
def drawSquares(screen):
	colors = [p.Color("tan1"), p.Color("rosybrown2")]
	for row in range(DIM):
		for col in range(DIM):
				color = colors[((col+row)%2)]
				p.draw.rect(screen, color, p.Rect(col*SQ_SIZE, row*SQ_SIZE, SQ_SIZE, SQ_SIZE))

def drawLastMove(screen, gs):
		color = p.Color("red")
		lastMove = gs.moveLog[len(gs.moveLog)-1]
		p.draw.rect(screen, color, p.Rect(lastMove.startCol*SQ_SIZE, lastMove.startRow*SQ_SIZE, SQ_SIZE, SQ_SIZE))
		p.draw.rect(screen, color, p.Rect(lastMove.endCol*SQ_SIZE, lastMove.endRow*SQ_SIZE, SQ_SIZE, SQ_SIZE))
				
def drawHighlightMoves(screen, gs, attackPiece):
	validMoves = gs.getValidMoves()
	if str(attackPiece) != '()':
		color = p.Color("palegoldenrod")
		for move in validMoves:
			if attackPiece[0] == move.startRow and attackPiece[1] == move.startCol:
				p.draw.rect(screen, color, p.Rect(move.endCol*SQ_SIZE, move.endRow*SQ_SIZE, SQ_SIZE, SQ_SIZE))
				
def drawLines(screen):
	color = p.Color("black")
	for row in range(1,DIM):
		for col in range(1,DIM):
				p.draw.line(screen, color, (col*SQ_SIZE, 0), (col*SQ_SIZE, WIDTH), 2)
				p.draw.line(screen, color, (0, row*SQ_SIZE), (HEIGHT, row*SQ_SIZE), 2)
	
def drawPieces(screen, board):
	for row in range(DIM):
		for col in range(DIM):
				piece = board[row][col]
				if piece != "-":
						screen.blit(IMAGES[piece], p.Rect(col*SQ_SIZE, row*SQ_SIZE, SQ_SIZE, SQ_SIZE))
                                							
if __name__ == "__main__":
	main()
