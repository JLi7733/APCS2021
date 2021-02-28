#Shogi - By Jonathan Li
#For those unfamiliar to Shogi, shogi is a game similar to chess mainly played in Japan
#Similar to chess the goal of shogi is to checkmate the opposing player's king
#There are many more differences between chess and shogi, so I'd reccomend one to read more about it here:
#https://www.shogi.cz/en/rules

#Where you left off last dum dum
#Just defined the pawn piece and it's moves now do the promoted pawns


#Step 1, defining your pieces

#The general class of piece that all other pieces will inherit from
class Piece:
    def __init__(self, team, xpos, ypos, promoted, board):
        self.team = team
        self.xPos = xpos
        self.yPos = ypos
        self.promoted = promoted
        self.board = board

#Pawn Piece
class Pawn(Piece):
    def __init__(self, team, xpos, ypos, promoted, board):
        super().__init__(team, xpos, ypos, promoted, board)
        self.name = Pawn
    
    #A Pawn's valid moves
    def validMoves(self):
        x = self.xPos
        y = self.yPos
        if(self.promoted):
            if(self.team == "white"):
                return
        else:
            if(self.team == "white"):
                return(x, y+1)
            else:
                return(x, y-1)

#Step 2, developing movement of pieces


#Step 3, promotion


#Step 4, checkmates and check


#Step 5 drawing the board and hands


#Step 6, making it interactive and making a GUI

#These are the variables and arrays we'll use to keep our game running and store our pieces
turn = 0
whiteHand = []
blackHand = []
board = []


#main program over here

p1 = Pawn("white", 1, 1, False, True)
x, y= p1.validMoves()
print(x," ", y)

