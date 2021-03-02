#Shogi - By Jonathan Li
#For those unfamiliar to Shogi, shogi is a game similar to chess mainly played in Japan
#Similar to chess the goal of shogi is to checkmate the opposing player's king
#There are many more differences between chess and shogi, so I'd reccomend one to read more about it here:
#https://www.shogi.cz/en/rules

#Where you left off last dum dum:
#Finally done with all the pieces classes, now go work on movement and taking pieces


#Step 1, defining your pieces

#The general class of piece that all other pieces will inherit from
class Piece:
    def __init__(self, team, position, promoted, board):
        self.team = team
        self.position = position
        self.promoted = promoted
        self.board = board
    def move(self, newPos):
        self.position = newPos


#Pawn Piece
class Pawn(Piece):
    def __init__(self, team, position, promoted, board):
        super().__init__(team, position, promoted, board)
        self.name = "Pawn"
    
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
            if(self.team):
                moves.append([x,y+1])            
            else:
                moves.append([x,y-1])
        return(moves)
#Knight Piece
class Knight(Piece):
    def __init__(self, team, position, promoted, board):
        super().__init__(team, position, promoted, board)
        self.name = "Knight"
    
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
            if(self.team):
                moves.append([x-1,y+2]) 
                moves.append([x+1, y+2])           
            else:
                moves.append([x-1,y-2])
                moves.append([x+1,y-2])
        return(moves)
#Lance Piece
class Lance(Piece):
    def __init__(self, team, position, promoted, board):
        super().__init__(team, position, promoted, board)
        self.name = "Lance"
    
    #A Lance's valid moves
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
            if(self.team):
                for y in range(y, 8):
                    y+=1
                    moves.append([x, y])           
            else:
                for y in range(1, y+1):
                    y-=1
                    moves.append([x, y])
        return(moves)
#Rook Piece
class Rook(Piece):
    def __init__(self, team, position, promoted, board):
        super().__init__(team, position, promoted, board)
        self.name = "Rook"
    
    #A Rook's valid moves
    def validMoves(self):
        #Defining the variables we'll need
        moves = []
        temp = self.position
        #Storing the values for x and y
        x = temp[0]
        y = temp[1]
        #Check if it's promoted or not
        if(self.promoted):
            moves = king(x, y)
        #Since a rook can move forward and backward we don't care which team it's on for moveset
        for y in range(-1,8):
            y+=1
            moves.append([x, y])
        y=temp[0]
        for x in range(-1, 8):
            x+=1
            moves.append([x, y])          
        
        #It'll repeat the square it's currently on so we have to remove that
        moves.remove([x,y])          

        return(moves)
#Bishop piece
class Bishop(Piece):
    def __init__(self, team, position, promoted, board):
        super().__init__(team, position, promoted, board)
        self.name = "Bishop"
    
    #A Bishop's valid moves
    def validMoves(self):
        #Defining the variables we'll need
        moves = []
        temp = self.position
        #Storing the values for x and y
        x = temp[0]
        y = temp[1]
        #Check if it's promoted or not
        if(self.promoted):
            moves = king(x, y)
        #Since a bishop can move forward and backward we don't care which team it's on for moveset
        temp = diagonals(temp, 9)
        moves = moves + temp

        moves.remove([x,y])          

        return(moves)
#Silver General
class Silver(Piece):
    def __init__(self, team, position, promoted, board):
        super().__init__(team, position, promoted, board)
        self.name = "Silver"
    
    def validMoves(self):
        #Defining the variables we'll need
        moves = []
        temp = self.position
        #Storing the values for x and y
        x = temp[0]
        y = temp[1]
        #Check if it's promoted or not
        moves = gold(x, y, self.team)
        moves.remove(x+1, y)
        moves.remove(x-1, y)
        if(self.team):
            moves.remove(x, y-1)
        else:
            moves.remove(x, y+1)
        return(moves)
#Golden General
class Gold(Piece):
    def __init__(self, team, position, promoted, board):
        super().__init__(team, position, promoted, board)
        self.name = "Gold"
    
    def validMoves(self):
        #Defining the variables we'll need
        moves = []
        temp = self.position
        #Storing the values for x and y
        x = temp[0]
        y = temp[1]
        #Check if it's promoted or not
        moves = gold(x, y, self.team)
        return(moves)
#King
class King(Piece):
    def __init__(self, team, position, promoted, board):
        super().__init__(team, position, promoted, board)
        self.name = "King"
    
    def validMoves(self):
        #Defining the variables we'll need
        moves = []
        temp = self.position
        #Storing the values for x and y
        x = temp[0]
        y = temp[1]
        moves = king(x, y)

        return(moves)

#Since when promoted a lot of pieces gain the moves of a gold general
#Instead of copypasting i made a function for that type of moveset
def gold(x, y, side):
    moves = []
    if (side):
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

#Same thing with the king moveset
def king(x, y):
    moves = []
    moves.append([x, y+1])
    moves.append([x+1, y+1])
    moves.append([x-1, y+1])
    moves.append([x-1, y])
    moves.append([x+1, y])
    moves.append([x, y-1])
    moves.append([x-1, y-1])
    moves.append([x+1, y-1])
    return moves

#Thank you very much to https://codereview.stackexchange.com/questions/146935/find-diagonal-positions-for-bishop-movement
#For the code, because I'm kinda lazy
def diagonals(coord, size):
    limit = size - 1
    coords = [coord]
    row = coord[0]
    col = coord[1]

    while row > 0 and col > 0:
        row -= 1
        col -= 1
        coords.append([row, col])

    row = coord[0]
    col = coord[1]

    while row < limit and col < limit:
        row += 1
        col += 1
        coords.append([row, col])

    row = coord[0]
    col = coord[1]

    while row < limit and col > 0:
        row += 1
        col -= 1
        coords.append([row, col])

    row = coord[0]
    col = coord[1]

    while row > 0 and col < limit:
        row -= 1
        col += 1
        coords.append([row, col])

    return coords


#Step 2, developing movement of pieces

#Let's check if your moves are even on the board
def onBoard(moves):
    for i in moves:
        x = i[0]
        y = i[1]
        if(x < 0 or x > 8 or y < 0 or y > 8):
            moves.remove(i)
    return(moves)

#The actual move function, aka moving and taking pieces
def movePiece(piece, finalPos, board):
    #First let's check is there another piece there?
    x = finalPos[0]
    y = finalPos[1]
    if(board[x][y]):
        print("yeet")

    #Ok, so let's get the piece we're moving and the place it's moving and do that
    piece.move(finalPos)



    




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

p1 = Bishop(True, [4,4], True, True)
temp = p1.validMoves()
print(temp)

