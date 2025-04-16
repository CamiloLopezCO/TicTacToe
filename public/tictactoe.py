import random

playerScore = 0
computerScore = 0

#3x3 board represented with a 2D list (rows x columns)
gameBoard = [['_', '|', '_', '|', '_'],
             ['_', '|', '_', '|', '_'],
             [' ', '|', ' ', '|', ' ']]

def printBoard(gameBoard):
    for row in gameBoard:
        print(''.join(row))

def getValidMoves(gameBoard):
    emptyCellsList = []
    for i in range(3):
        for j in range(5):
            if gameBoard[i][j] in ('_', ' '):
                emptyCellsList.append([i, j])
    return emptyCellsList

def updateBoard(position, player, gameBoard):
    character = 'X' if player == 1 else 'O'
    
    pos_map = {
        1: (0, 0), 2: (0, 2), 3: (0, 4),
        4: (1, 0), 5: (1, 2), 6: (1, 4),
        7: (2, 0), 8: (2, 2), 9: (2, 4)
    }

    if position in pos_map:
        row, col = pos_map[position]
        gameBoard[row][col] = character
        printBoard(gameBoard)

def playerMove(gameBoard):
    print("Please make a move. (1-9)")
    
    move = int(input())

    while not isValidMove(move, gameBoard):
        print("Sorry! Invalid Move. Try again")
        move = int(input())

    print(f"Player moved at position {move}")
    updateBoard(move, 1, gameBoard)

def isValidMove(move, gameBoard):
    pos_map = {
        1: (0, 0), 2: (0, 2), 3: (0, 4),
        4: (1, 0), 5: (1, 2), 6: (1, 4),
        7: (2, 0), 8: (2, 2), 9: (2, 4)
    }

    if move in pos_map:
        row, col = pos_map[move]
        return gameBoard[row][col] in ('_', ' ')
    return False

def cloneArray(src):
    return [row[:] for row in src]

#Added helper to check if board is full
def isBoardFull(gameBoard):
    return all(gameBoard[i][j] != '_' and gameBoard[i][j] != ' ' for i in range(3) for j in [0,2,4])

def minimaxDecision(gameBoard):
    currentUtility = float('-inf')
    emptyCellList = getValidMoves(gameBoard)
    moveList = None
    cutOff = 5 #Depth limit for search

    for row in emptyCellList:
        alpha = float('-inf')
        beta = float('inf')
        copyBoard = cloneArray(gameBoard)
        move = indexToMove(row)
        updateBoard(move, 2, copyBoard)  # Making call with player as computer
        utility = minValue(copyBoard, alpha, beta, cutOff - 1)

        if utility > currentUtility:
            currentUtility = utility
            moveList = row

    return moveList

#MAX Computer's turn
def maxValue(gameBoard, alpha, beta, depth):
    score = evaluationFunction(gameBoard)
    if abs(score) == 1.0 or isBoardFull(gameBoard) or depth == 0:
        return score
    
    v = float('-inf')
    for move in getValidMoves(gameBoard):
        copyBoard = cloneArray(gameBoard)
        updateBoard(indexToMove(move), 2, copyBoard)
        v = max(v, minValue(copyBoard, alpha, beta, depth - 1))
        if v >= beta:
            return v # Beta cutoff
        alpha = max(alpha, v)
    return v

#MIN Player's turn
def minValue(gameBoard, alpha, beta, depth):
    score = evaluationFunction(gameBoard)
    if abs(score) == 1.0 or isBoardFull(gameBoard) or depth == 0:
        return score
    
    v = float('inf')
    for move in getValidMoves(gameBoard):
        copyBoard = cloneArray(gameBoard)
        updateBoard(indexToMove(move), 1, copyBoard)
        v = min(v, maxValue(copyBoard, alpha, beta, depth - 1))
        if v <= alpha:
            return v # Alpha cutoff
        beta = min(beta, v)
    return v

#Improved evaluation function (with non-terminal state scoring)
def evaluationFunction(board):
    lines = [
        [(0,0),(0,2),(0,4)], #Row
        [(1,0),(1,2),(1,4)],
        [(2,0),(2,2),(2,4)],
        [(0,0),(1,0),(2,0)], #Columns
        [(0,2),(1,2),(2,2)],
        [(0,4),(1,4),(2,4)],
        [(0,0),(1,2),(2,4)], #Diagonals
        [(2,0),(1,2),(0,4)],
    ]

    score = 0
    for line in lines:
        values = [board[i][j] for i,j in line]
        if values.count('O') == 3:
            return 1.0
        elif values.count('X') == 3:
            return  -1.0
        elif values.count('O') == 2 and values.count('_') + values.count(' ') == 1:
            score += 0.5
        elif values.count('X') == 2 and values.count('_') + values.count(' ') == 1:
            score -= 0.5
    return score

def indexToMove(moveList):
    pos_map = {
        (0, 0): 1, (0, 2): 2, (0, 4): 3,
        (1, 0): 4, (1, 2): 5, (1, 4): 6,
        (2, 0): 7, (2, 2): 8, (2, 4): 9
    }
    return pos_map.get(tuple(moveList), 0)

def computerMove(gameBoard):
    nextMove = minimaxDecision(gameBoard)
    move = indexToMove(nextMove)
    print(f"Computer moved at position {move}")
    updateBoard(move, 2, gameBoard)

def isGameOver(gameBoard):
    global playerScore, computerScore
    # Check for win conditions
    score = evaluationFunction(gameBoard)
    if score == -1.0:
        print("Player Wins")
        playerScore += 1
        return True
    if score == 1.0:
        print("Computer Wins")
        computerScore += 1
        return True
    if score == 0.0 and isBoardFull(gameBoard):
        print("It's a tie")
        return True

    return False

def resetBoard(gameBoard):
    gameBoard[0][0] = '_'
    gameBoard[0][2] = '_'
    gameBoard[0][4] = '_'
    gameBoard[1][0] = '_'
    gameBoard[1][2] = '_'
    gameBoard[1][4] = '_'
    gameBoard[2][0] = ' '
    gameBoard[2][2] = ' '
    gameBoard[2][4] = ' '
"""
    Notes:

        _ | _ | _
        _ | _ | _
          |   |

         Helpful indices

         [0][0] , [0][2] , [0][4]
         [1][0] , [1][2] , [1][4]
         [2][0] , [2][2] , [2][4]

        Player = 1
        Computer = 2

 """
#Game loop
if __name__ == "__main__":
    printBoard(gameBoard)
    playAgain = True

    while playAgain:
        gameOver = False
        while not gameOver:
            playerMove(gameBoard)
            gameOver = isGameOver(gameBoard)
            if gameOver:
                break

            computerMove(gameBoard)
            gameOver = isGameOver(gameBoard)

        print(f"Player Score: {playerScore}")
        print(f"Computer Score: {computerScore}")
        result = input("Would you like to play again? (Y/N): ").strip().lower()

        if result == 'y':
            playAgain = True
            print("Yes! Let's play again")
            resetBoard(gameBoard)
            printBoard(gameBoard)
        else:
            playAgain = False
            print("Thanks for playing")