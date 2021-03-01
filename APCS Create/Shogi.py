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
    def __init__(self, team, position, promoted, board):
        self.team = team
        self.position = position
        self.promoted = promoted
        self.board = board

#Pawn Piece
class Pawn(Piece):
    def __init__(self, team, position, promoted, board):
        super().__init__(team, position, promoted, board)
        self.name = Pawn
    
    #A Pawn's valid moves
    def validMoves(self):
        #Defining the variables we'll need
        moves = []
        temp = self.position
        #Storing the values for x and y
        x = temp[0]
        y = temp[1]
        #Check if it's promoted or not
        if(self.promoted):
            #Check which team it's on
            moves = gold(x, y, self.team)
        else:
            if(self.team == "white"):
                moves.append([x,y+1])            
            else:
                moves.append([x,y-1])
        return(moves)

#Step 2, developing movement of pieces

#Let's check if your moves are even valid
def onBoard(moves):
    for i in moves:
        x = i[0]
        y = i[1]
        if(x < 0 or x > 8 or y < 0 or y > 8):
            moves.remove(i)
    return(moves)

#Since when promoted a lot of pieces gain the moves of a gold general
#Instead of copypasting i made a function for that type of moveset
def gold(x, y, side):
    moves = []
    if (side == "white"):
        moves.append([x, y+1])
        moves.append([x+1, y+1])
        moves.append([x-1, y+1])
        moves.append([x-1, y])
        moves.append([x+1, y])
        moves.append([x, y-1])
    else:
        moves.append([x, y-1])
        moves.append([x+1, y-1])
        moves.append([x-1, y-1])
        moves.append([x-1, y])
        moves.append([x+1, y])
        moves.append([x, y+1]) 
    return moves



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

p1 = Pawn("white", [1,1], True, True)
temp = p1.validMoves()
print(temp)

