from move import Move
import random

import sys

class GameState():

	#init board
	def __init__(self):
		self.board = [["-", "-", "-", "-", "bk", "-", "-", "-"],
						["-", "-", "wq", "-", "-", "-", "-", "-",],
						["-", "-", "-", "-", "-", "-", "-", "-",],
						["-", "-", "-", "-", "-", "-", "-", "-",],
						["-", "-", "-", "-", "-", "-", "-", "-",],
						["-", "-", "-", "-", "-", "-", "-", "-",],
						["-", "-", "-", "-", "-", "-", "-", "-",],
						["-", "-", "-", "-", "wk", "-", "-", "-"]]
			
		'''
		[["br", "bn", "bb", "bq", "bk", "bb", "bn", "br"],
						["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
						["-", "-", "-", "-", "-", "-", "-", "-",],
						["-", "-", "-", "-", "-", "-", "-", "-",],
						["-", "-", "-", "-", "-", "-", "-", "-",],
						["-", "-", "-", "-", "-", "-", "-", "-",],
						["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
						["wr", "wn", "wb", "wq", "wk", "wb", "wn", "wr"]]
		'''
		
		
		self.rowNotation = ["8", "7", "6", "5", "4", "3", "2", "1"]
		self.colNotation = ["a", "b", "c", "d", "e", "f", "g", "h"]
		self.notationLog = []
		
		#variables for castling
		self.whiteKingMoved = False
		self.leftWhiteRookMoved = False
		self.rightWhiteRookMoved = False
		
		self.blackKingMoved =  False
		self.leftBlackRookMoved = False
		self.rightBlackRookMoved = False
		
		#gamestate variables
		self.checkmate = False
		self.stalemate = False
		self.whiteMove = True #keep track of turn
		self.moveLog = [] #store track of all moves
		self.whiteKingLoc = (7, 4)
		self.blackKingLoc = (0, 4)
		


	def makeMove(self, move, validMoves):
		notation = "Null"
		#EN PASSANT
		if move.flag == 1: #flag 1 = white en passant left
			self.board[move.startRow][move.startCol] = "-"
			self.board[move.startRow][move.startCol-1] = "-"
			self.board[move.endRow][move.endCol] = move.pieceMoved
			
			startCol = self.colNotation[move.startCol]
			endRow = self.rowNotation[move.endRow]
			endCol = self.colNotation[move.endCol]
			notation = startCol + "x"  + endCol + endRow
			
		elif move.flag == 2: #flag 2 = white en passant right
			self.board[move.startRow][move.startCol] = "-"
			self.board[move.startRow][move.startCol+1] = "-"
			self.board[move.endRow][move.endCol] = move.pieceMoved
			
			startCol = self.colNotation[move.startCol]
			endRow = self.rowNotation[move.endRow]
			endCol = self.colNotation[move.endCol]
			notation = startCol + "x" + endCol + endRow
			
		elif move.flag == 3: #flag 3 = black en passant left
			self.board[move.startRow][move.startCol] = "-"
			self.board[move.startRow][move.startCol-1] = "-"
			self.board[move.endRow][move.endCol] = move.pieceMoved
			
			startCol = self.colNotation[move.startCol]
			endRow = self.rowNotation[move.endRow]
			endCol = self.colNotation[move.endCol]
			notation = startCol + "x" + endCol + endRow 
			
		elif move.flag == 4: #flag 4 = black en passant right
			self.board[move.startRow][move.startCol] = "-"
			self.board[move.startRow][move.startCol+1] = "-"
			self.board[move.endRow][move.endCol] = move.pieceMoved
			
			startCol = self.colNotation[move.startCol]
			endRow = self.rowNotation[move.endRow]
			endCol = self.colNotation[move.endCol]
			notation = startCol + "x" + endCol + endRow 
			
		#WHITE CASTLING
		elif move.flag == 8: #flag 8 = white castle left
			self.board[move.startRow][move.startCol] = "-"
			self.board[move.endRow][move.endCol] = move.pieceMoved
			self.board[7][0] = "-"
			self.board[7][3] = "wr"
			
			notation = "O-O-O"
			
		elif move.flag == 9: #flag 9 = white castle right
			self.board[move.startRow][move.startCol] = "-"
			self.board[move.endRow][move.endCol] = move.pieceMoved
			self.board[7][7] = "-"
			self.board[7][5] = "wr"
			
			notation = "O-O"
			
		#BLACK CASTLING
		elif move.flag == 13: #flag 13 = black castle left
			self.board[move.startRow][move.startCol] = "-"
			self.board[move.endRow][move.endCol] = move.pieceMoved
			self.board[0][0] = "-"
			self.board[0][3] = "br"
			
			notation = "O-O-O"
			
		elif move.flag == 14: #flag 14 = black castle right
			self.board[move.startRow][move.startCol] = "-"
			self.board[move.endRow][move.endCol] = move.pieceMoved
			self.board[0][7] = "-"
			self.board[0][5] = "br"
			
			notation = "O-O"
		
		else:
			self.board[move.startRow][move.startCol] = "-"
			self.board[move.endRow][move.endCol] = move.pieceMoved
			
			#CHESS NOTATION
			startRow = self.rowNotation[move.startRow]
			startCol = self.colNotation[move.startCol]
			endRow = self.rowNotation[move.endRow]
			endCol = self.colNotation[move.endCol]
			pieceCaptured = False if move.pieceCaptured == "-" else True
			
			#PAWN NOTATION
			if move.pieceMoved[1] == "p":
				#Regular notation	
				if pieceCaptured:
					notation = startCol + 'x' + endCol + endRow
				else:
					notation = endCol + endRow
				#pawn promotion
				if move.endRow == 7:
					self.board[move.endRow][move.endCol] = 'bq'
					if pieceCaptured:
						notation = startCol + 'x' + endCol + endRow + '=Q'
					else:
						notation = endCol + endRow + '=Q'
				elif move.endRow == 0:
					self.board[move.endRow][move.endCol] = 'wq'
					if pieceCaptured:
						notation = startCol + 'x' + endCol + endRow + '=Q'
					else:
						notation = endCol + endRow + '=Q'
					
			#REGULAR KING/QUEEN/BISHOP NOTATION
			elif move.pieceMoved[1] == "k" or move.pieceMoved[1] == "q" or move.pieceMoved[1] == "b":
				if pieceCaptured:
					notation = move.pieceMoved[1].upper() + 'x' + endCol + endRow
				else:
					notation = move.pieceMoved[1].upper() + endCol + endRow
			
			#REGULAR KNIGHT NOTATION
			elif move.pieceMoved[1] == "n":
				isAmbiguous = False
				isColAmbiguous = False
				for checkMove in validMoves:
					if move.moveID != checkMove.moveID and move.endRow == checkMove.endRow and move.endCol == checkMove.endCol and checkMove.pieceMoved[1] == "n":
						isAmbiguous = True
						if move.startCol == checkMove.startCol:
							isColAmbiguous = True
						
				if isAmbiguous:
					if isColAmbiguous:
						if pieceCaptured:
							notation = move.pieceMoved[1].upper() + startRow + 'x' + endCol + endRow
						else:
							notation = move.pieceMoved[1].upper() + startRow + endCol + endRow
					else:
						if pieceCaptured:
							notation = move.pieceMoved[1].upper() + startCol + 'x' + endCol + endRow
						else:
							notation = move.pieceMoved[1].upper() + startCol + endCol + endRow
				else:
					if pieceCaptured:
						notation = move.pieceMoved[1].upper() + 'x' + endCol + endRow
					else:
						notation = move.pieceMoved[1].upper() + endCol + endRow
			
			#REGULAR ROOK NOTATION
			elif move.pieceMoved[1] == "r":
				isAmbiguous = False
				isColAmbiguous = False
				for checkMove in validMoves:
					if move.moveID != checkMove.moveID and move.endRow == checkMove.endRow and move.endCol == checkMove.endCol and checkMove.pieceMoved[1] == "r":
						isAmbiguous = True
						if move.startCol == checkMove.startCol:
							isColAmbiguous = True
						
				if isAmbiguous:
					if isColAmbiguous:
						if pieceCaptured:
							notation = move.pieceMoved[1].upper() + startRow + 'x' + endCol + endRow
						else:
							notation = move.pieceMoved[1].upper() + startRow + endCol + endRow
					else:
						if pieceCaptured:
							notation = move.pieceMoved[1].upper() + startCol + 'x' + endCol + endRow
						else:
							notation = move.pieceMoved[1].upper() + startCol + endCol + endRow
							
				else:
					if pieceCaptured:
						notation = move.pieceMoved[1].upper() + 'x' + endCol + endRow
					else:
						notation = move.pieceMoved[1].upper() + endCol + endRow
		
		self.moveLog.append(move) #log move so we can undo
		self.whiteMove = not self.whiteMove #switch players	
		
		if self.inCheck():
			notation = notation + "+"
			self.notationLog.append(notation)
		else:
			self.notationLog.append(notation)
		
		#WHITE CASTLING
		if move.flag == 5: #flag 5 = white rook left first move
			self.leftWhiteRookMoved = True
		elif move.flag == 6: #flag 6 = white rook right first move
			self.rightWhiteRookMoved = True
		elif move.flag == 7 or move.flag == 8 or move.flag == 9: #flag 7,8,9 = white king first moved or castled
			self.whiteKingMoved = True
		#BLACK CASTLING
		elif move.flag == 10: #flag 10 = black rook left first move
			self.leftBlackRookMoved = True
		elif move.flag == 11: #flag 11 = black rook right first move
			self.rightBlackRookMoved = True
		elif move.flag == 12 or move.flag == 13 or move.flag == 14: #flag 12,13,14 = black king first moved or castled
			self.blackKingMoved = True
		
		#update king
		if move.pieceMoved == 'wk':
			self.whiteKingLoc = (move.endRow, move.endCol)
			self.whiteKingMoved = True
		if move.pieceMoved == 'bk':
			self.blackKingLoc = (move.endRow, move.endCol)
			self.blackKingMoved =  True
			
	
	def undoMove(self):
		if(len(self.moveLog) != 0):
			move = self.moveLog.pop()
			self.notationLog.pop()
						
			#EN PASSANT
			if move.flag == 1:
				self.board[move.startRow][move.startCol] = move.pieceMoved
				self.board[move.endRow][move.endCol] = move.pieceCaptured
				self.board[move.startRow][move.startCol-1] = "bp"
			elif move.flag == 2:
				self.board[move.startRow][move.startCol] = move.pieceMoved
				self.board[move.endRow][move.endCol] = move.pieceCaptured
				self.board[move.startRow][move.startCol+1] = "bp"
			elif move.flag == 3:
				self.board[move.startRow][move.startCol] = move.pieceMoved
				self.board[move.endRow][move.endCol] = move.pieceCaptured
				self.board[move.startRow][move.startCol-1] = "wp"
			elif move.flag == 4:
				self.board[move.startRow][move.startCol] = move.pieceMoved
				self.board[move.endRow][move.endCol] = move.pieceCaptured
				self.board[move.startRow][move.startCol+1] = "wp"
			
			#WHITE CASTLING
			elif move.flag == 8:
				self.board[move.startRow][move.startCol] = move.pieceMoved
				self.board[move.endRow][move.endCol] = "-"
				self.board[7][0] = "wr"
				self.board[7][3] = "-"
			elif move.flag == 9:
				self.board[move.startRow][move.startCol] = move.pieceMoved
				self.board[move.endRow][move.endCol] = "-"
				self.board[7][7] = "wr"
				self.board[7][5] = "-"
			#BLACK CASTLING
			elif move.flag == 13:
				self.board[move.startRow][move.startCol] = move.pieceMoved
				self.board[move.endRow][move.endCol] = "-"
				self.board[0][0] = "br"
				self.board[0][3] = "-"
			elif move.flag == 14:
				self.board[move.startRow][move.startCol] = move.pieceMoved
				self.board[move.endRow][move.endCol] = "-"
				self.board[0][7] = "br"
				self.board[0][5] = "-"
				
			else: #original move
				self.board[move.startRow][move.startCol] = move.pieceMoved
				self.board[move.endRow][move.endCol] = move.pieceCaptured
			
			#CASTLING TRACKING
			if move.flag == 5:
				self.leftWhiteRookMoved = False
			elif move.flag == 6:
				self.rightWhiteRookMoved = False
			elif move.flag == 7 or move.flag == 8 or move.flag == 9:
				self.whiteKingMoved = False
			elif move.flag == 10:
				self.leftBlackRookMoved = False
			elif move.flag == 11:
				self.rightBlackRookMoved = False
			elif move.flag == 12 or move.flag == 13 or move.flag == 14:
				self.blackKingMoved = False
				
			#update king
			if move.pieceMoved == 'wk':
				self.whiteKingLoc = (move.startRow, move.startCol)
			if move.pieceMoved == 'bk':
				self.blackKingLoc = (move.startRow, move.startCol)
				
			self.whiteMove = not self.whiteMove
			
	def getValidMoves(self):
		#1. generate all possible moves
		moves = self.getAllPossibleMoves()
		#2. for each move, 
		for i in range(len(moves)-1, -1, -1): #transverse list backwards so we can delete if need be safely
			#3. generate all opponents moves
			self.makeMove(moves[i], moves)
			#4. for each of opponents moves, see if they attack your king
			self.whiteMove = not self.whiteMove
			if self.inCheck():
				moves.remove(moves[i]) #5. if they do attack your king that move is not valid
			self.whiteMove = not self.whiteMove
			self.undoMove()
		if len(moves) == 0 or self.isOtherStalemate(): #either checkmate or stalemate
			if self.inCheck():
				self.checkmate = True
				lastMove = self.notationLog.pop()
				lastMove = lastMove[0:len(lastMove)-1] + '#'
				self.notationLog.append(lastMove)
				if self.whiteMove:
					notation = '0-1'
				else:
					notation = '1-0'
			else:
				self.stalemate = True
				notation = '.5-.5'
				
			self.notationLog.append(notation)
			sys.stdout.write(str(self.notationLog)+"\n")
			sys.stdout.flush()
			self.writeResults()			
				
		else:
			self.checkmate = False
			self.stalemate = False
			
		return moves


	'''
	#THREEFOLD REPETITION
	#FIFTY-MOVE RULE
	'''		
	def isOtherStalemate(self):
		oneKnight = False
		
		oneWhiteBishop = False
		whiteBishopOddLocation = False
		whiteBishopEvenLocation = False
		
		oneBlackBishop = False
		blackBishopOddLocation = False
		blackBishopEvenLocation = False
		
		onlyKing = True
		
		#Impossibility of checkmate
		for row in range(0,8):
			for col in range(0,8):
				if self.board[row][col] != '-':
				
					#IF ANYTHING OTHER THAN KING/BISHOP/KNIGHT
					if self.board[row][col][1] != 'k' and self.board[row][col][1] != 'b' and self.board[row][col][1] != 'n':
						return False
					
					elif self.board[row][col][1] == 'n' and oneKnight:
						return False
					elif self.board[row][col][1] == 'n':
						oneKnight = True
						
					elif self.board[row][col] == 'wb':
						if oneWhiteBishop == True:
							return False
						elif oneWhiteBishop == False:
							oneWhiteBishop = True
							if ((col+row)%2) == 0:
								whiteBishopEvenLocation = True
							else:
								whiteBishopOddLocation = True
						
					elif self.board[row][col] == 'bb':
						if oneBlackBishop == True:
							return False
						elif oneBlackBishop == False:
							oneBlackBishop = True
							if ((col+row)%2) == 0:
								blackBishopEvenLocation = True
							else:
								blackBishopOddLocation = True
					if self.board[row][col][1] != 'k':
						onlyKing = False
						
		
		#K,B vs K,B (Bishops on same color)
		if (blackBishopEvenLocation and whiteBishopEvenLocation) or (blackBishopOddLocation and whiteBishopOddLocation):
			return True
		#K vs K,B
		if (oneBlackBishop and not oneWhiteBishop) or (oneWhiteBishop and not oneBlackBishop):
			return True
		#K vs K,N 
		elif oneKnight:
			return True
		#K vs K
		elif onlyKing:
			return True
		else:
			return False
	
	
	#check if current player is in check
	def inCheck(self):
		if self.whiteMove:
			return self.squareUnderAttack(self.whiteKingLoc[0], self.whiteKingLoc[1])
		else:
			return self.squareUnderAttack(self.blackKingLoc[0], self.blackKingLoc[1])
		
		
	#see if enemy can attack this squareUnderAttack
	def squareUnderAttack(self, r, c):
		self.whiteMove = not self.whiteMove
		oppMoves = self.getAllPossibleMoves()
		self.whiteMove = not self.whiteMove
		for move in oppMoves:
			if move.endRow == r and move.endCol == c: ## square under attack
				return True
		return False
	
	#scan all of board and get list of all possible moves not checking for self check
	def getAllPossibleMoves(self):
		moves = []
		for r in range(len(self.board)): 
			for c in range(len(self.board[r])):
				turn = self.board[r][c][0]
				if (turn == 'w' and self.whiteMove) or (turn == 'b' and not self.whiteMove):
					piece = self.board[r][c][1]
					self.getMoves(piece,r, c, moves)
		return moves
		
	#return all moves possible for such piece not checking for self check
	def getMoves(self, piece, r, c, moves):
		enemyColor = "b" if self.whiteMove else "w"
		allyColor = "b" if enemyColor == "w" else "w"
		
		#PAWN MOVEMENT
		if piece == 'p':
			#white pawn moves
			if allyColor == "w":
				#move forward
				if self.board[r-1][c] == "-":
					moves.append(Move((r, c), (r-1, c), self.board, 0))
					if r == 6 and self.board[r-2][c] == "-":
						moves.append(Move((r, c), (r-2, c), self.board, 0))
				#capture enemy piece
				if c-1 >= 0: #capture to left
					if self.board[r-1][c-1][0] == 'b':
						moves.append(Move((r, c), (r-1, c-1), self.board, 0))
				if c+1 <= 7: #capture to right
					if self.board[r-1][c+1][0] == 'b':
						moves.append(Move((r, c), (r-1, c+1), self.board, 0))	
				#en-passant 
				if len(self.moveLog) != 0:
					lastMove = self.moveLog[len(self.moveLog)-1]
					if lastMove.pieceMoved == 'bp' and lastMove.endRow - lastMove.startRow == 2:
						if r == lastMove.endRow:
							if c-1 == lastMove.endCol and self.board[r-1][c-1][0] != 'w':
								moves.append(Move((r, c), (r-1, c-1), self.board, 1))
							if c+1 == lastMove.endCol and self.board[r-1][c+1][0] != 'w':
								moves.append(Move((r, c), (r-1, c+1), self.board, 2))
							
				
			#black pawn moves			
			else:
				#move forwards
				if self.board[r+1][c] == "-":
					moves.append(Move((r, c), (r+1, c), self.board, 0))
					if r == 1 and self.board[r+2][c] == "-":
						moves.append(Move((r, c), (r+2, c), self.board, 0))
				#capture enemy piece		
				if c-1 >= 0: #capture to left
					if self.board[r+1][c-1][0] == 'w':
						moves.append(Move((r, c), (r+1, c-1), self.board, 0))
				if c+1 <= 7: #capture to right
					if self.board[r+1][c+1][0] == 'w':
						moves.append(Move((r, c), (r+1, c+1), self.board, 0))
				#en-passant 
				if len(self.moveLog) != 0:
					lastMove = self.moveLog[len(self.moveLog)-1]
					if lastMove.pieceMoved == 'wp' and lastMove.startRow - lastMove.endRow == 2:
						if r == lastMove.endRow:
							if c-1 == lastMove.endCol and self.board[r+1][c-1][0] != allyColor:
								moves.append(Move((r, c), (r+1, c-1), self.board, 3))
							if c+1 == lastMove.endCol and self.board[r+1][c+1][0] != allyColor:
								moves.append(Move((r, c), (r+1, c+1), self.board, 4))
						
		#KNIGHT MOVEMENT
		elif piece == 'n':
			directions = ((-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1))
			for d in directions:
				endRow = r + d[0]
				endCol = c + d[1]
				if 0 <= endRow < 8 and 0 <= endCol < 8:
					endPiece = self.board[endRow][endCol]
					if endPiece[0] != allyColor: #empty or enemy piece
						moves.append(Move((r, c), (endRow, endCol), self.board, 0))
						
		#KING MOVEMENT
		elif piece == 'k':
			directions = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
			pieceNameColor = allyColor + piece
			for i in range(8):
				endRow = r + directions[i][0]
				endCol = c + directions[i][1]
				if 0 <= endRow < 8 and 0 <= endCol < 8:
					endPiece = self.board[endRow][endCol]
					if endPiece[0] != allyColor: #empty or enemy space
						if self.whiteKingMoved == False and pieceNameColor == "wk":
							moves.append(Move((r, c), (endRow, endCol), self.board, 7))
						elif self.blackKingMoved == False and pieceNameColor == "bk":
							moves.append(Move((r, c), (endRow, endCol), self.board, 12))
						else:
							moves.append(Move((r, c), (endRow, endCol), self.board, 0))
							
			#WHITE CASTLING
			if pieceNameColor == "wk" and self.whiteKingMoved == False and self.inCheck == False:
				if self.leftWhiteRookMoved == False and self.board[7][1] == '-' and self.board[7][2] == '-' and self.board[7][3] == '-':
					moves.append(Move((r, c), (7, 2), self.board, 8))
				if self.rightWhiteRookMoved == False and self.board[7][5] == '-' and self.board[7][6] == '-':
					moves.append(Move((r, c), (7, 6), self.board, 9))
			#BLACK CASTLING
			if pieceNameColor == "bk" and self.blackKingMoved == False and self.inCheck == False:
				if self.leftBlackRookMoved == False and self.board[0][1] == '-' and self.board[0][2] == '-' and self.board[0][3] == '-':
					moves.append(Move((r, c), (0, 2), self.board, 13))
				if self.rightBlackRookMoved == False and self.board[0][5] == '-' and self.board[0][6] == '-':
					moves.append(Move((r, c), (0, 6), self.board, 14))
				
						
		#BISHOP/QUEEN MOVEMENT
		if piece == 'b' or piece == 'q':
			directions = ((-1, -1), (-1, 1), (1, -1), (1, 1))
			for d in directions:
				for i in range(1, 8):
					endRow = r + d[0] * i
					endCol = c + d[1] * i
					if 0 <= endRow < 8 and 0 <= endCol < 8:
						endPiece = self.board[endRow][endCol]
						if endPiece == "-":
							moves.append(Move((r, c), (endRow, endCol), self.board, 0))
						elif endPiece[0] == enemyColor:
							moves.append(Move((r, c), (endRow, endCol), self.board, 0))
							break;
						else: #friendly piece
							break
					else: # off board
						break
						
		#ROOK/QUEEN MOVEMENT
		if piece == 'r' or piece == 'q':
			pieceNameColor = allyColor + piece
			directions = ((-1, 0), (0, -1), (1, 0), (0, 1)) #up, left, down, right
			for d in directions:
				for i in range(1, 8):
					endRow = r + d[0] * i
					endCol = c + d[1] * i
					if 0 <= endRow < 8 and  0 <= endCol < 8: #on board
						endPiece = self.board[endRow][endCol]
						if endPiece == "-": #open spot
							if pieceNameColor == "wr" and self.leftWhiteRookMoved == False and r == 7 and c == 0:
								moves.append(Move((r, c), (endRow, endCol), self.board, 5))
							elif pieceNameColor == "wr" and self.rightWhiteRookMoved == False and r == 7 and c == 7:
								moves.append(Move((r, c), (endRow, endCol), self.board, 6))
							elif pieceNameColor == "br" and self.leftBlackRookMoved == False and r == 0 and c == 0:
								moves.append(Move((r, c), (endRow, endCol), self.board, 10))
							elif pieceNameColor == "br" and self.rightBlackRookMoved == False and r == 0 and c == 7:
								moves.append(Move((r, c), (endRow, endCol), self.board, 11))
							else:
								moves.append(Move((r, c), (endRow, endCol), self.board, 0))
						elif endPiece[0] == enemyColor: #enemy spot
							if pieceNameColor == "wr" and self.leftWhiteRookMoved == False and r == 7 and c == 0:
								moves.append(Move((r, c), (endRow, endCol), self.board, 5))
							elif pieceNameColor == "wr" and self.rightWhiteRookMoved == False and r == 7 and c == 7:
								moves.append(Move((r, c), (endRow, endCol), self.board, 6))
							elif pieceNameColor == "br" and self.leftBlackRookMoved == False and r == 0 and c == 0:
								moves.append(Move((r, c), (endRow, endCol), self.board, 10))
							elif pieceNameColor == "br" and self.rightBlackRookMoved == False and r == 0 and c == 7:
								moves.append(Move((r, c), (endRow, endCol), self.board, 11))
							else:
								moves.append(Move((r, c), (endRow, endCol), self.board, 0))
							break
						else: #friendly piece
							break
					else: #off board
						break

	#write results to file after game is over with move log and winner
	def writeResults(self):
		fname = 'gameHistory.py'
		with open(fname, 'a') as f:
			f.write('game = {}\n'.format(self.notationLog))

	#if color = a AI vs AI, color = w W vs AI, color = b B vs AI		
	def AI(self, moves):
		goodMoves = []
		
		for move in moves:
			#check if can attack piece
			if move.pieceCaptured != "-":
				goodMoves.append(move)
				
		
		if len(goodMoves) != 0:
			rNum = random.randint(0,len(goodMoves)-1)
			self.makeMove(goodMoves[rNum], moves)
		else:
			rNum = random.randint(0,len(moves)-1)
			self.makeMove(moves[rNum], moves)
		