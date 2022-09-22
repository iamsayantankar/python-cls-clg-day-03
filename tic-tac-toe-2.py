while (True):
    print("Start the game now...\nY for yes\nN for no.\nEnter your choise:")
    startGame = input()
    if (startGame == "Y"):

        theBoard = {'1': ' ', '2': ' ', '3': ' ', '6': ' ', '5': ' ',
                    '4': ' ', '7': ' ', '8': ' ', '9': ' '}


        def printBoard(board):
            print(board['1'] + '|' + board['2'] + '|' + board['3'])
            print('-+-+-')
            print(board['4'] + '|' + board['5'] + '|' + board['6'])
            print('-+-+-')
            print(board['7'] + '|' + board['8'] + '|' + board['9'])


        turn = "X"
        for i in range(10):
            printBoard(theBoard)
            if ((theBoard["1"] == "X" and theBoard["2"] == "X" and theBoard["3"] == "X") or (
                    theBoard["7"] == "X" and theBoard["8"] == "X" and theBoard["9"] == "X") or (
                    theBoard["4"] == "X" and theBoard["5"] == "X" and theBoard["6"] == "X") or (
                    theBoard["1"] == "X" and theBoard["4"] == "X" and theBoard["7"] == "X") or (
                    theBoard["2"] == "X" and theBoard["5"] == "X" and theBoard["8"] == "X") or (
                    theBoard["3"] == "X" and theBoard["6"] == "X" and theBoard["9"] == "X") or (
                    theBoard["1"] == "X" and theBoard["5"] == "X" and theBoard["9"] == "X") or (
                    theBoard["3"] == "X" and theBoard["5"] == "X" and theBoard["7"] == "X")):
                print("X s winer")
                break
            if ((theBoard["1"] == "O" and theBoard["2"] == "O" and theBoard["3"] == "O") or (
                    theBoard["7"] == "O" and theBoard["8"] == "O" and theBoard["9"] == "O") or (
                    theBoard["4"] == "O" and theBoard["5"] == "O" and theBoard["6"] == "O") or (
                    theBoard["1"] == "O" and theBoard["4"] == "O" and theBoard["7"] == "O") or (
                    theBoard["2"] == "O" and theBoard["5"] == "O" and theBoard["8"] == "O") or (
                    theBoard["3"] == "O" and theBoard["6"] == "O" and theBoard["9"] == "O") or (
                    theBoard["1"] == "O" and theBoard["5"] == "O" and theBoard["9"] == "O") or (
                    theBoard["3"] == "O" and theBoard["5"] == "O" and theBoard["7"] == "O")):
                print("O s winer")
                break
            if (theBoard["1"] != " " and theBoard["2"] != " " and theBoard["3"] != " " and
                    theBoard["7"] != " " and theBoard["8"] != " " and theBoard["9"] != " " and
                    theBoard["4"] != " " and theBoard["5"] != " " and theBoard["6"] != " "):
                print("Match is draw...")
                break
            print("Turn for " + turn + " . Move on which space?")
            move = input()
            while (True):
                if (
                        move == "1" or move == "2" or move == "3" or move == "6" or move == "5" or move == "4" or move == "7" or move == "8" or move == "9"):
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
        # printBoard(theBoard)
    elif (startGame == "N"):
        break
    else:
        print("Pleaser enter the right value...")
