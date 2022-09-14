EMPTY = None

class GameState:
    def __init__(self):
        self.board = ["R", "N", "B", "Q", "K", "B", "N", "R",
                      "P", "P", "P", "P", "P", "P", "P", "P",
                      EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY,
                      EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY,
                      EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY,
                      EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY,
                      "p", "p", "p", "p", "p", "p", "p", "p",
                      "r", "n", "b", "q", "k", "b", "n", "r"]
        
        self.WhiteToMove = True
        self.WhiteCanCastleKingside = False
        self.WhiteCanCastleQueenside = False
        self.BlackCanCastleKingside = False
        self.BlackCanCastleQueenside = False
        

class Piece:
    def __init__(self, id, square):
        self.id = id
        self.square = square
        
    def getIdentifier(self):
        return self.id
    
    def getSquare(self):
        return self.square
    
    def getType(self):
        if (self.id == None):
            return "Empty Square"
        if (self.id.lower() == 'r'):
            return "Rook"
        if (self.id.lower() == 'n'):
            return "Knight"
        if (self.id.lower() == 'b'):
            return "Bishop"
        if (self.id.lower() == 'q'):
            return "Queen"
        if (self.id.lower() == 'k'):
            return "King"
        if (self.id.lower() == 'p'):
            return "Pawn"
        
    def getColor(self):
        
        if(self.id == None):
            return None
        
        if (self.id.isupper()):
            return "White"
        else:
            return "Black"
    
    #returns a list of pseudolegal target squares    
    #def getPseudoLegal(self):
        
        
        
            

        
#returns a string with square notation
def toSquare(id):    
    return chr((id % 8) + 97) + str(int(id/8) + 1)
        
def onBoard(square_id):
    if (square_id >= 0 & square_id <= 63):
        return True
    else:
        return False



    
    
       

      
def main():    
    game = GameState()
    piece = Piece(game.board[3], 3)
    
    


if __name__ == "__main__":
    main()
   