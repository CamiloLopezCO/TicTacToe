# Tic Tac Toe AI with Minimax and Alpha-Beta Pruning

This project is a Python implementation of the classic Tic Tac Toe game, 
enhanced with an AI opponent powered by the Minimax algorithm and alpha-beta pruning. 
The game begins with a standard 3x3 board where the player (X) competes against the computer (O). 
I began with a starter codebase and modified it to implement adversarial search strategies, 
including complete `minValue()` and `maxValue()` functions that explore game states up to a defined 
depth limit.
I also improved the evaluation function to handle non-terminal states, 
allowing the computer to make smarter decisions even when the board is not in a winning or 
losing state. 
These changes enable the AI to look ahead, prune suboptimal branches, 
and play competitively against a baseline "rookie" agent. 
The final result is an interactive and intelligent Tic Tac Toe game playable in the terminal.

