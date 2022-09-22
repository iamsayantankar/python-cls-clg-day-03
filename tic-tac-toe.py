while (True):
    print("Start the game now...\nY for yes\nN for no.\nEnter your choise:")
    startGame = input()
    if (startGame == "Y"):

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
            if ((theBoard["top-L"] == "X" and theBoard["top-M"] == "X" and theBoard["top-R"] == "X") or (
                    theBoard["low-L"] == "X" and theBoard["low-M"] == "X" and theBoard["low-R"] == "X") or (
                    theBoard["mid-L"] == "X" and theBoard["mid-M"] == "X" and theBoard["mid-R"] == "X") or (
                    theBoard["top-L"] == "X" and theBoard["mid-L"] == "X" and theBoard["low-L"] == "X") or (
                    theBoard["top-M"] == "X" and theBoard["mid-M"] == "X" and theBoard["low-M"] == "X") or (
                    theBoard["top-R"] == "X" and theBoard["mid-R"] == "X" and theBoard["low-R"] == "X") or (
                    theBoard["top-L"] == "X" and theBoard["mid-M"] == "X" and theBoard["low-R"] == "X") or (
                    theBoard["top-R"] == "X" and theBoard["mid-M"] == "X" and theBoard["low-L"] == "X")):
                print("X s winer")
                break
            if ((theBoard["top-L"] == "O" and theBoard["top-M"] == "O" and theBoard["top-R"] == "O") or (
                    theBoard["low-L"] == "O" and theBoard["low-M"] == "O" and theBoard["low-R"] == "O") or (
                    theBoard["mid-L"] == "O" and theBoard["mid-M"] == "O" and theBoard["mid-R"] == "O") or (
                    theBoard["top-L"] == "O" and theBoard["mid-L"] == "O" and theBoard["low-L"] == "O") or (
                    theBoard["top-M"] == "O" and theBoard["mid-M"] == "O" and theBoard["low-M"] == "O") or (
                    theBoard["top-R"] == "O" and theBoard["mid-R"] == "O" and theBoard["low-R"] == "O") or (
                    theBoard["top-L"] == "O" and theBoard["mid-M"] == "O" and theBoard["low-R"] == "O") or (
                    theBoard["top-R"] == "O" and theBoard["mid-M"] == "O" and theBoard["low-L"] == "O")):
                print("O s winer")
                break
            if (theBoard["top-L"] != " " and theBoard["top-M"] != " " and theBoard["top-R"] != " " and
                    theBoard["low-L"] != " " and theBoard["low-M"] != " " and theBoard["low-R"] != " " and
                    theBoard["mid-L"] != " " and theBoard["mid-M"] != " " and theBoard["mid-R"] != " "):
                print("Match is draw...")
                break
            print("Turn for " + turn + " . Move on which space?")
            move = input()
            while (True):
                if (
                        move == "top-L" or move == "top-M" or move == "top-R" or move == "mid-R" or move == "mid-M" or move == "mid-L" or move == "low-L" or move == "low-M" or move == "low-R"):
                    break
                else:
                    print("Turn for " + turn + " . Move on which space?")
                    move = input()
            while (True):
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
    elif (startGame == "N"):
        break
    else:
        print("Pleaser enter the right value...")
