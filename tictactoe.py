"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    xcount = 0
    ocount = 0
    
    for i in range(len(board)):
        for j in range(len(board[1])):
            if board[i][j] == 'X':
                xcount += 1
            elif (board[i][j] == 'O'):
                ocount += 1
        
    if xcount > ocount:
        return "O"
    else:
        return "X"



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    
    actions = set()
    for i in range(len(board)):
        for j in range(len(board[1])):
            temp_tuple = ()
            if board[i][j] == EMPTY:
                temp_tuple = (i,j)
                actions.add(temp_tuple)
        
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    
    
    new_board = copy.deepcopy(board)
    
    if board[action[0]][action[1]] != None:
        raise ValueError
    try:    
        new_board[action[0]][action[1]] = player(board)
    
    except:
        raise ValueError
    
    return new_board
    


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    
    
    #checks rows
    for i in range(len(board)):
        if board[i][0] == board[i][1] and board[i][0] == board[i][2]:
            return board[i][0]
         
    #checks columns
    for i in range(len(board[0])):
        if board[0][i] == board[1][i] and board[0][i] == board[2][i]:
            return board[0][i]
     
    
    #checks diagonals
    
    if (board[1][1] == board[0][0] and board[1][1] == board[2][2]) or (board[1][1] == board[0][2] and board[1][1] == board[2][0]):
        return board[1][1]

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
 
    if (winner(board) == None) and len(actions(board)) != 0:
        return False
    else:
        return True
    
    


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    
    if winner(board) == X:
        return 1
    elif winner(board) == O:
      
        return -1
    else:
        return 0
   

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    
    #checks for completed board
    if(terminal(board)):
        return None

    #assigns what a good score is based on whose turn it is
    if player(board) == X:
        good_score = 1
    else:
        good_score = -1
    
    #finds a list of total actions and defaults to first item
    total_actions = list(actions(board))
    best_action = total_actions[0]

    #if the board is empty, the computer chooses the top left place
    if len(total_actions) == 9:
        return (0,0)
        
    #this for-loop is technically unnecessary, but makes the computer player "more human".
    #Specifically, in a scenario when multiple forced-wins are availabe from the computer's
    #point of view, it will prioritize an immediate win
    for i in range(len(total_actions)):
        score = utility(result(board,total_actions[i]))
        if(score == good_score):
            return total_actions[i]
        
    #for-loop iterates through all possible actions
    for i in range(len(total_actions)):
    
        #initializes temporary board for given total action
        temp_board = result(board,total_actions[i])
    
        #while loop continues to modify board with optimal moves until game is completed
        while not terminal(temp_board):
            temp_board = result(temp_board,minimax(temp_board))
            
        score = utility(temp_board)
        
        #an optimal score is returned immediately
        if score == good_score:
            #if(len(total_actions) == 5):
                #print(temp_board)
                #print(board)
                #print(f'good score found at {total_actions[i]}')
            return total_actions[i]
        
        #A move which causes a tie is remembered, but will be "overwritten" by an optimal game move
        elif score == 0:
            best_action = total_actions[i]                  
    
    return best_action
            
