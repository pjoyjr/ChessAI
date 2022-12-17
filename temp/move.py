class Move():
	
	def __init__(self, startSq, endSq, board, flag):
		self.startRow = startSq[0]
		self.startCol = startSq[1]
		self.endRow = endSq[0]
		self.endCol = endSq[1]
		self.pieceMoved = board[self.startRow][self.startCol]
		self.pieceCaptured = board[self.endRow][self.endCol]
		self.moveID = self.startRow + self.startCol * 10 + self.endRow * 100 + self.endCol * 1000
		self.flag = flag
		
	
	def __eq__(self, other):
		if isinstance(other, Move):
			return self.moveID == other.moveID
		return False