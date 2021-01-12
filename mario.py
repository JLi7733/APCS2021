
#get the height
level = input("Height: ")
height = 0
currentrow = 1
getInput = True


while(getInput):
    try:
        height = int(level) + 1
    except:
        print("Please enter a valid number")
        level = input("Height: ")
    else:
        getInput = False


#print the thing
for currentrow in range(height):
    print(" "*(height-currentrow) + "#" * currentrow + "  " + "#" * currentrow)

        




