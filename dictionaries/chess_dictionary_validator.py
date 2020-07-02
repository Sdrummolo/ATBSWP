# Write a function named isValidChessBoard() that takes a dictionary argument and returns True or False depending on if the board is valid. A valid board will have exactly one black king and exactly one white king. Each player can only have at most 16 pieces, at most 8 pawns, and all pieces must be on a valid space from '1a' to '8h'; that is, a piece can’t be on space '9z'. The piece names begin with either a 'w' or 'b' to represent white or black, followed by 'pawn', 'knight', 'bishop', 'rook', 'queen', or 'king'. This function should detect when a bug has resulted in an improper chess board.

def isValidChessBoard(board):
  if type(board) != dict:
    return False

  legalPositions = ["a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "b1", "b2", "b3", "b4", "b5", "b6", "b7", "b8", "c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "d1", "d2", "d3", "d4", "d5", "d6", "d7", "d8", "e1", "e2", "e3", "e4", "e5", "e6", "e7", "e8", "f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8", "g1", "g2", "g3", "g4", "g5", "g6", "g7", "g8", "h1", "h2", "h3", "h4", "h5", "h6", "h7", "h8", ]
  colors = ["w", "b"]
  pieces = ["pawn", "knight", "bishop", "rook", "queen", "king"]
  bKing = False
  wKing = False
  bPawns = 0
  wPawns = 0
  totWhites = 0
  totBlacks = 0

  for position, piece in board.items():
    position = position.lower()
    piece = piece.lower()

    if position not in legalPositions:
      return False
    if piece[0] not in colors:
      return False
    if piece[1:] not in pieces:
      return False
    if piece == "bking":
      if bKing == True:
        return False
      else:
        bKing = True
        totBlacks += 1
        continue
    if piece == "wking":
      if wKing == True:
        return False
      else:
        wKing = True
        totWhites += 1
        continue
    if piece == "bpawn":
      bPawns += 1
      totBlacks += 1
      continue
    if piece == "wpawn":
      wPawns += 1
      totWhites += 1
      continue
    if piece[0] == "b":
      totBlacks += 1
    elif piece[0] == "w":
      totWhites += 1

  if bKing == False or wKing == False:
    return False
  if bPawns > 8 or wPawns > 8:
    return False
  if totBlacks > 16 or totWhites > 16:
    return False

  return True
  

print(isValidChessBoard({"h1": "bking", "c6": "wqueen", "g2": "bbishop", "h5": "bqueen", "e3": "wking", "a2": "bpawn"}))  # True
print(isValidChessBoard({"a1": "bpawn", "a2": "wking"}))  # False: no bking
print(isValidChessBoard({"a1": "wking", "a2": "wking", "c3": "bbishop"}))  # False: cannot have 2 white kings, no bking
print(isValidChessBoard({"a1": "bking", "z9": "wking"}))  # False: z9 is an invalid position
print(isValidChessBoard({'a1':'bking','a2':'wking','h1':'bpawn','h2':'bpawn','h3':'bpawn','h4':'bpawn','h5':'bpawn','h6':'bpawn','h7':'bpawn','h8':'bpawn','g7':'bpawn','g8':'bpawn'}))#False theres more than 8 pawns
print(isValidChessBoard({"a1": "wking", "a2": "wking", "c3": "bbishop", "c4": "bking"})) # False: cannot have 2 white kings and 1 black king