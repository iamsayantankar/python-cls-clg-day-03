theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 'mid-R': ' ', 'mid-M': ' ',
            'mid-L': ' ', 'low-L': ' ', 'low-M': ' ', 'low-M': ' ', 'low-R': ' '}


def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])


turn = "X"
for i in range(9):
    printBoard(theBoard)
    print("Turn for " + turn + " . Move on which space?")
    move = input()
    while(True):
        if (move == "top-L" or move == "top-M" or move == "top-R" or move == "mid-R" or move == "mid-M" or move == "mid-L" or move == "low-L" or move == "low-M" or move == "low-R"):
            break
        else:
            print("Turn for " + turn + " . Move on which space?")
            move = input()
    while(True):
        if (theBoard[move] == " "):
            break
        else:
            print("Please enter wirgt input.\nTurn for " + turn + " . Move on which space?")
            move = input()
    theBoard[move] = turn
    if turn == "X":
        turn = "O"
    else:
        turn = "X"
printBoard(theBoard)

if((theBoard["top-L"]=="X" and theBoard["top-M"]=="X" and theBoard["top-R"]=="X" ) or (theBoard["low-L"]=="X" and theBoard["low-M"]=="X" and theBoard["low-R"]=="X" ) or (theBoard["mid-L"]=="X" and theBoard["mid-M"]=="X" and theBoard["mid-R"]=="X" ) or (theBoard["top-L"]=="X" and theBoard["mid-L"]=="X" and theBoard["low-L"]=="X" ) or (theBoard["top-M"]=="X" and theBoard["mid-M"]=="X" and theBoard["low-M"]=="X" ) or (theBoard["top-R"]=="X" and theBoard["mid-R"]=="X" and theBoard["low-R"]=="X" ) or (theBoard["top-L"]=="X" and theBoard["mid-M"]=="X" and theBoard["low-R"]=="X" ) or (theBoard["top-r"]=="X" and theBoard["mid-M"]=="X" and theBoard["low-L"]=="X" )):
    print("X s winer")
if((theBoard["top-L"]=="X" and theBoard["top-M"]=="X" and theBoard["top-R"]=="X" ) or (theBoard["low-L"]=="X" and theBoard["low-M"]=="X" and theBoard["low-R"]=="X" ) or (theBoard["mid-L"]=="X" and theBoard["mid-M"]=="X" and theBoard["mid-R"]=="X" ) or (theBoard["top-L"]=="X" and theBoard["mid-L"]=="X" and theBoard["low-L"]=="X" ) or (theBoard["top-M"]=="X" and theBoard["mid-M"]=="X" and theBoard["low-M"]=="X" ) or (theBoard["top-R"]=="X" and theBoard["mid-R"]=="X" and theBoard["low-R"]=="X" ) or (theBoard["top-L"]=="X" and theBoard["mid-M"]=="X" and theBoard["low-R"]=="X" ) or (theBoard["top-r"]=="X" and theBoard["mid-M"]=="X" and theBoard["low-L"]=="X" )):
    print("X s winer")
