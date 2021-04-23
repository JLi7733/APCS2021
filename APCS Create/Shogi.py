#Shogi - By Jonathan Li
#For those unfamiliar to Shogi, shogi is a game similar to chess mainly played in Japan
#Similar to chess the goal of shogi is to checkmate the opposing player's king
#There are many more differences between chess and shogi, so I'd reccomend one to read more about it here:
#https://www.shogi.cz/en/rules

#Where you left off last dum dum:
#Did all the display business, now let's actually go do movement

#Step 1, defining your pieces

#Dictionary for 

#The general class of piece that all other pieces will inherit from
class Piece:
    def __init__(self, team, position, promoted, board):
        self.team = team
        self.position = position
        self.promoted = promoted
        self.board = board
    def move(self, newPos):
        self.position = newPos
    
    #Function one can call to promote your piece, and later on also change images
    def promote(self):
        self.promoted = True

#Pawn Piece
class Pawn(Piece):
    def __init__(self, team, position, promoted, board):
        super().__init__(team, position, promoted, board)
        self.name = "Pawn"
        self.img = "\u6B69"
    
    #A Pawn's valid moves
    def possibleMoves(self):
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
                moves.append([x-1,y])            
            else:
                moves.append([x+1,y])
        moves = onBoard(moves)
        return(moves)
    
    def promote(self):
        super.promote(self)
        self.img = '\u3068'
    
    def draw(self):
        return(self.img)
#Knight Piece
class Knight(Piece):
    def __init__(self, team, position, promoted, board):
        super().__init__(team, position, promoted, board)
        self.name = "Knight"
        self.img = "\u6842"
    
    def possibleMoves(self):
        moves = []
        temp = self.position
        x = temp[0]
        y = temp[1]
        if(self.promoted):
            moves = gold(x, y, self.team)
        else:
            if(self.team):
                moves.append([x-2,y+1]) 
                moves.append([x-2,y-1])           
            else:
                moves.append([x+2,y-1])
                moves.append([x+1,y-1])
        moves = onBoard(moves)
        return(moves)

    def promote(self):
        super.promote(self)
        self.img = '\u572D'
#Lance Piece
class Lance(Piece):
    def __init__(self, team, position, promoted, board):
        super().__init__(team, position, promoted, board)
        self.name = "Lance"
        self.img = "\u9999"
    
    #A Lance's valid moves
    def possibleMoves(self, board):
        moves = []
        temp = self.position
        x = temp[0]
        y = temp[1]
        if(self.promoted):
            moves = gold(x, y, self.team)
        else:
            if(self.team):
                for x in range(0, x):
                    x-=1
                    if(board[x][y] == 0):
                        moves.append([x, y])
                    else:
                        break           
            else:
                for x in range(x, 8):
                    x-=1
                    if(board[x][y] == 0):
                        moves.append([x, y])
                    else:
                        break     
        moves = onBoard(moves)
        return(moves)
    
    def promote(self):
        super.promote(self)
        self.img = '\u4EDD'
#Rook Piece
class Rook(Piece):
    def __init__(self, team, position, promoted, board):
        super().__init__(team, position, promoted, board)
        self.name = "Rook"
        self.img = "\u98DB"
    
    #A Rook's valid moves
    def possibleMoves(self):
        moves = []
        index = self.position
        x = index[0]
        y = index[1]
        if(self.promoted):
            moves = king(x, y)
        else:
            #Get all the possible moves for a rook through pure spaghetti code
            cross = []
            temp = []
            #right
            for i in range(1, 9-y):
                boomer = [x, y+i]
                temp.append(boomer)
            cross.append(temp)
            temp = []
            #left
            for i in range(1, y+1):
                boomer = [x, y-i]
                temp.append(boomer)
            cross.append(temp)
            temp = []
            #up
            for i in range(1, 9-x):
                boomer = [x+i, y]
                temp.append(boomer)
            cross.append(temp)
            temp = []
            #down
            for i in range(1, x+1):
                boomer = [x-i, y]
                temp.append(boomer)
            cross.append(temp)
            #Some weird shit to try and find where the possible moves are, we try each direction and 
            #break if there is a piece there
            for direction in cross:
                for position in direction:
                    if(board[position[0]][position[1]] == 0):
                        moves.append(position)
                    elif board[position[0]][position[1]].team == False:
                        print(board[position[0]][position[1]])
                        moves.append(position)
                        break
                    else:
                        break
        return(moves)

    def promote(self):
        super.promote(self)
        self.img = '\u9F8D'
#Bishop piece
class Bishop(Piece):
    def __init__(self, team, position, promoted, board):
        super().__init__(team, position, promoted, board)
        self.name = "Bishop"
        self.img = "\u89D2"
    
    #A Bishop's valid moves
    def possibleMoves(self):
        moves = []
        temp = self.position
        x = temp[0]
        y = temp[1]
        if(self.promoted):
            moves = king(x, y)
        else:
            temp = diagonals(temp, 9)
            for direction in temp:
                for position in direction:
                    if board[position[0]][position[1]] == 0:
                        moves.append(position)
                    elif board[position[0]][position[1]].team == False:
                        print(board[position[0]][position[1]])
                        moves.append(position)
                        break
                    else:
                        break

        return(moves)
    
    def promote(self):
        super.promote(self)
        self.img = '\u99AC'
#Silver General
class Silver(Piece):
    def __init__(self, team, position, promoted, board):
        super().__init__(team, position, promoted, board)
        self.name = "Silver"
        self.img = "\u9280"
    
    def possibleMoves(self):
        moves = []
        temp = self.position
        x = temp[0]
        y = temp[1]
        moves = gold(x, y, self.team)
        moves.remove([x, y-1])
        moves.remove([x, y+1])
        if(self.team):
            moves.remove([x+1, y])
            moves.append([x+1, y-1])
            moves.append([x+1, y+1])
        else:
            moves.remove([x-1, y])
            moves.append([x-1, y-1])
            moves.append([x-1, y+1])
        moves = onBoard(moves)
        return(moves)

    def promote(self):
        super.promote(self)
        self.img = '\u5168'
#Golden General
class Gold(Piece):
    def __init__(self, team, position, promoted, board):
        super().__init__(team, position, promoted, board)
        self.name = "Gold"
        self.img = "\u91D1"
    
    def possibleMoves(self):
        moves = []
        temp = self.position
        x = temp[0]
        y = temp[1]
        moves = gold(x, y, self.team)
        return(moves)
#King
class King(Piece):
    def __init__(self, team, position, promoted, board):
        super().__init__(team, position, promoted, board)
        self.name = "King"
        if(self.team):
            self.img = "\u6842"
        else:
            self.img = "\u7389"
    
    def possibleMoves(self):
        moves = []
        temp = self.position
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
        moves.append([x-1, y+1])
        moves.append([x-1, y-1])
        moves.append([x-1, y])
        moves.append([x+1, y])
        moves.append([x, y-1])
    else:
        moves.append([x, y-1])
        moves.append([x+1, y-1])
        moves.append([x+1, y+1])
        moves.append([x-1, y])
        moves.append([x+1, y])
        moves.append([x, y+1]) 
    moves = onBoard(moves)
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
    moves = onBoard(moves)
    return moves

def diagonals(coord, size):
    limit = size - 1
    coords = []
    row = coord[0]
    col = coord[1]
    temp = []

    while row > 0 and col > 0:
        row -= 1
        col -= 1
        temp.append([row, col])

    coords.append(temp)
    temp = []
    row = coord[0]
    col = coord[1]

    while row < limit and col < limit:
        row += 1
        col += 1
        temp.append([row, col])

    coords.append(temp)
    temp = []
    row = coord[0]
    col = coord[1]

    while row < limit and col > 0:
        row += 1
        col -= 1
        temp.append([row, col])

    coords.append(temp)
    temp = []
    row = coord[0]
    col = coord[1]

    while row > 0 and col < limit:
        row -= 1
        col += 1
        temp.append([row, col])
    coords.append(temp)
    return coords
#Step 2, developing movement of pieces

#Let's check if your moves are even on the board
def onBoard(moves):
    print(moves)
    for i in moves:
        x = i[0]
        y = i[1]
        print(x, y)
        if(x < 0):
            moves.remove(i)
        elif(x > 8):
            moves.remove(i)
        elif(y < 0):
            moves.remove(i)
        elif(y > 8):
            moves.remove(i)
    return(moves)

#The actual move function, aka moving and taking pieces
def movePiece(board):
    #First let's check what is the piece and which team
    valid = True
    while(valid):
        row = int(input("What row is your piece on: "))-1
        col = int(input("What column is your piece on: "))-1
        if(board[row][col] != 0):
            valid = False
    initx = row
    inity = col
    piece = board[row][col]
    team = piece.team
    validMoves = piece.possibleMoves()
    valid = True
    while(valid):
        inputy = True
        while(inputy):
            x = int(input("Which row do you want to move to: "))-1
            y = int(input("which column do you want to move to: "))-1
            print(validMoves)
            if([x,y] in validMoves):
                inputy = False
        #Now, let's check if there is a piece there
        if(board[x][y] != 0):
            #If there is a piece there, we now have to check if it's the same team or not
            if(board[x][y].team != team):
                #We should add the taken piece to the other's hand
                if(team):
                    whiteHand.append(board[x][y])
                else:
                    blackHand.append(board[x][y])

                board[x][y].board = False
                board[x][y].promted = False
                board[x][y].team = not(board[x][y].team)
            else:
                #Since it's not the right piece let's just return an error and stop the function
                valid = True
        board[x][y] = piece
        board[initx][inity].position = [x, y]
        board[initx][inity] = 0
        valid = False

    
    return board
        
 

    #Ok, so let's get the piece we're moving and the place it's moving and do that

#Step 3, promotion and returning a piece to the board

def checkPromote(piece):
    position = piece.position
    pieceType = piece.name
    yPos = position[1]
    if(piece.promoted):
        return(False)
    else:
        if(pieceType != "King" and pieceType != "Gold"):
            if(piece.team):
                return(yPos > 5)
            else:
                return(yPos < 3)
        else:
            return(False)       

def promote(board):
    valid = True
    promote = 
    while(valid):
        row = int(input("What row is your piece on: "))-1
        col = int(input("What column is your piece on: "))-1
        if(board[row][col] != 0):
            valid = False
    
    piece = board[row][col]
    if


def placeHand(piece, board):
    loop = True
    while(loop):
        x = int(input("Which row: "))-1
        y = int(input("Which column: "))-1
        if piece.name == "Pawn" or piece.name == "Lance":
            if(piece.team):
                if(x < 8):
                    loop = False
            else:
                if(x > 0):
                    loop = False
        elif piece.name == "Knight":
            if(piece.team):
                if(x < 7):
                    loop = False
            else:
                if(x > 1):
                    loop = False

    board[x][y] = piece
    
#Step 4, checkmates and check

def checkmate(board, side):
    moves = []
    status = ""
    #First we locate the king, and all the possible moves of the opposing team
    for j in board:
        for i in j:
            if i != 0:
                if i.team == side:
                    if i.name == "King":
                        temp = i
                if i.team != side:
                    moves.append(i.possibleMoves())
    #Then we generate an array of all the king's possible moves
    kingMoves = temp.possibleMoves()
    kingMoves.append(temp.position)
    print(moves)
    #If a piece can move to the place where the king is, we delete it
    for j in moves:
        for i in j:
            if (i == temp.position):
                print(i)
                status = "check"
                kingMoves.remove(i)
            if (i in kingMoves):
                kingMoves.remove(i)
                print(i)
    #if the king can no longer move, it's checkmate
    if(len(kingMoves) == 0):
        return True
    else:
        print(kingMoves)
        return False



    return True

#Step 5 drawing the board and hands

def displayBoard(board):
    row = 1
    print("     1      2      3      4      5      6      7      8      9")
    for x in board:
        print(row, " ", end = "")
        row+=1
        for tile in x:
            if(tile == 0):
                print("||  ||", end = " ")
            else:
                text = tile.img
                print("||", end="")
                print(text, end = "")
                print("||", end = " ")
        
        print("")
    
    print("")


#main program over here

#first we define some generic variables and arrays, our hands, our board, and the turn count
turn = True
whiteHand = []
blackHand = []
board = [[0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0], 
         [0,0,0,0,0,0,0,0,0], 
         [0,0,0,0,0,0,0,0,0], 
         [0,0,0,0,0,0,0,0,0], 
         [0,0,0,0,0,0,0,0,0], 
         [0,0,0,0,0,0,0,0,0]]

#Now we fill said board
board[8][0] = Rook(True, [8, 0], False, True)
board[7][0] = Rook(True, [7, 0], False, True)
board[8][8] = King(False, [8,8], False, True)
whiteHand.append(Pawn(True, [0,0], True, False))

#Introduction
print("Hello and welcome to my game of shogi, if you want to know more about how this game works go here")
print("https://www.shogi.cz/en/rules")
playGame = True
temp = True
while(playGame):
    displayBoard
    while(temp):
        user = input("Do you want to move, promote, or place a piece back? ")
        if(user = "move"):
            movePiece(board)
        elif(user = "promote"):

