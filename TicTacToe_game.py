import sys
import random


#Cell on the board class
class Cell:
     def __init__(self,x=-1,y=-1):
         self.x = x
         self.y = y


#Printing the board
def PrintGame(TicTacToeMatrix):
    PrintHeadLine()
    for i in range(0,3):
        sys.stdout.write (str(i+1))    
        sys.stdout.write('|')
        for j in range (0,3):
            if TicTacToeMatrix[i][j]=='X':
                sys.stdout.write(' X |')
            elif TicTacToeMatrix[i][j]=='O':
                sys.stdout.write(' O |')
            else:
                sys.stdout.write('   |')
        sys.stdout.write('\n')

#printing the numbers in the first row
def PrintHeadLine():
    print("\n   1   2   3")

#Printing the introduction
def PrintPregame():
    print("\nWelcome to TicTacToe!")
    pawn = (input("Please choose X/O:  "))
    while (pawn != 'X' and pawn != 'O'):
        pawn = (input("Please choose only X/O!:  "))
    return pawn

#receiving from the user an input choice
def InputInt(string):
    print(string)
    inp = input()
    try:
         res = int (inp)
         return res
    except:
        return -1

#Making the Player Move
def MyMove(TicTacToeMatrix,MyPawn):
    cellChoice = Cell()
    #Getting from the User the next move
    print("now its your turn to choose an empty cell!")
    cellChoice.x = InputInt("please select row number between 1 and 3:  ")-1
    cellChoice.y=  InputInt("please select col number between 1 and 3:  ")-1
    while (cellChoice.x < 0 or cellChoice.x > 2 or cellChoice.y < 0 or cellChoice.y > 2) or  TicTacToeMatrix[cellChoice.x][cellChoice.y] != " ":
        print("Only natural number between 1 and 3 are allowed! also check if the cell is empty!")
        cellChoice.x=InputInt("please select row number between 1 and 3:  ")-1
        cellChoice.y=InputInt("please select col number between 1 and 3:  ")-1
    
    TicTacToeMatrix[cellChoice.x][cellChoice.y] = MyPawn
    if isWon(TicTacToeMatrix,MyPawn,cellChoice):
        return True
    elif isTied(TicTacToeMatrix):
        return True
    else:
        return False

#checking if Pawn Won
def isWon (TicTacToeMatrix,Pawn,cellChoice) :
    if(TicTacToeMatrix[cellChoice.x][0] == Pawn and TicTacToeMatrix[cellChoice.x][1] == Pawn and TicTacToeMatrix[cellChoice.x][2] == Pawn):
        print("\n",Pawn,"WON!!!")
        return True

    if(TicTacToeMatrix[0][cellChoice.y] == Pawn and TicTacToeMatrix[1][cellChoice.y] == Pawn and TicTacToeMatrix[2][cellChoice.y] == Pawn):
        print("\n",Pawn,"WON!!!")
        return True

    if cellChoice.x==cellChoice.y or cellChoice.x == 2 - cellChoice.y:
        if ((TicTacToeMatrix[0][0] == Pawn and TicTacToeMatrix[1][1] == Pawn and TicTacToeMatrix[2][2] == Pawn)
        or  (TicTacToeMatrix[0][2] == Pawn and TicTacToeMatrix[1][1] == Pawn and TicTacToeMatrix[2][0] == Pawn)):
            print("\n",Pawn,"WON!!!")
            return True

    else:
        return False

#Checking for a Tie
def isTied (TicTacToeMatrix):
    for i in range(0,3):
        for j in range(0,3):
            if TicTacToeMatrix[i][j] == " ":
                return False
    print("\nTIED!!!")
    return True

#Called when its the computer's turn
def ComputerMove(TicTacToeMatrix,MyPawn,OposPawn): 
    #if the computer almost winning  
    TargetCell = oneStepFromWin(TicTacToeMatrix,OposPawn)
    if TargetCell.x != -1 and TargetCell.y != -1:
        TicTacToeMatrix[TargetCell.x][TargetCell.y] = OposPawn
        print("\n",OposPawn,"WON!!!")
        return True
    #if the User almost winning
    TargetCell = oneStepFromWin(TicTacToeMatrix,MyPawn)

    if TargetCell.x != -1 and TargetCell.y != -1:
        TicTacToeMatrix[TargetCell.x][TargetCell.y] = OposPawn
        return isTied (TicTacToeMatrix)

    TargetCell = RandCell(TicTacToeMatrix)
    TicTacToeMatrix[TargetCell.x][TargetCell.y] = OposPawn
    return isTied (TicTacToeMatrix)

#returning a random empty cell
def RandCell(TicTacToeMatrix):
    EmptyPosList = []
    for i in range (0,3):
        for j in range (0,3):
            if (TicTacToeMatrix[i][j] == " "):
                EmptyPosList.append(Cell(i,j))

    return random.choice(EmptyPosList)



#checking if Pawn is one step from winning the game
def oneStepFromWin(TicTacToeMatrix,Pawn):
    TargetCellRow = Cell()
    TargetCellCol = Cell()
    counterPawnRow = 0
    counterSpaceRow = 0
    counterPawnCol = 0
    counterSpaceCol = 0
    for i in range(0,3):
        for j in range(0,3):
            #Row check
            if (TicTacToeMatrix[i][j] == Pawn):
                counterPawnRow += 1
            if (TicTacToeMatrix[i][j] == " "):
                counterSpaceRow += 1
                TargetCellRow = Cell(i,j)
            if (TicTacToeMatrix[j][i] == Pawn):
                #Col check
                counterPawnCol += 1
            if (TicTacToeMatrix[j][i] == " "):
                counterSpaceCol += 1
                TargetCellCol = Cell(j,i)

        if counterPawnRow == 2 and counterSpaceRow == 1:
            return TargetCellRow
        elif counterPawnCol == 2 and counterSpaceCol == 1:
            return TargetCellCol
        else:
            counterPawnRow = 0
            counterSpaceRow = 0
            counterPawnCol = 0
            counterSpaceCol = 0


    TargetCellRB = Cell()
    TargetCellLB = Cell()
    counterPawnLB = 0
    counterSpaceLB = 0
    counterPawnRB = 0
    counterSpaceRB = 0
    #diagonal lines check            
    for i in range(0,3):
        if (TicTacToeMatrix[i][i] == Pawn):
            counterPawnLB += 1
        if (TicTacToeMatrix[i][i] == " "):
            counterSpaceLB += 1
            TargetCellLB = Cell(i,i)
        if (TicTacToeMatrix[2-i][i] == Pawn):
            counterPawnRB += 1
        if (TicTacToeMatrix[2-i][i] == " "):
            counterSpaceRB += 1
            TargetCellRB = Cell(2-i,i)

    if counterPawnLB == 2 and counterSpaceLB == 1:
        return TargetCellLB
    elif counterPawnRB == 2 and counterSpaceRB == 1:
        return TargetCellRB
    else:
        return Cell()





#MAIN
GameOver = False
TicTacToeMatrix = [[" "," "," "],[" "," "," "],[" "," "," "]]
MyPawn = PrintPregame()

if MyPawn == 'X':
    OposPawn = 'O'
else:
    OposPawn = 'X'


while not GameOver:
    if MyPawn == 'X':
       PrintGame(TicTacToeMatrix)
       GameOver = MyMove(TicTacToeMatrix,MyPawn)
       if GameOver == True:
           PrintGame(TicTacToeMatrix)
           print("\nGAME OVER")
           continue

       GameOver = ComputerMove(TicTacToeMatrix,MyPawn,OposPawn)
       if GameOver == True:
           PrintGame(TicTacToeMatrix)
           print("\nGAME OVER")
           
    else:
        GameOver = ComputerMove(TicTacToeMatrix,MyPawn,OposPawn)
        if GameOver == True:
           PrintGame(TicTacToeMatrix)
           print("\nGAME OVER")
           continue
        PrintGame(TicTacToeMatrix)
        GameOver = MyMove(TicTacToeMatrix,MyPawn)
        if GameOver == True:
           PrintGame(TicTacToeMatrix)
           print("\nGAME OVER")
           
