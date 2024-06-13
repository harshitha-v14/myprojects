#!/usr/bin/env python
# coding: utf-8

# In[43]:


#importing all required libraries
import numpy as np
import random
from time import sleep


# In[44]:


# creating an empty tic-tac-toe board
def empty_board():
    board =np.array([
                     [0,0,0],
                     [0,0,0],
                     [0,0,0],
                     ])
    return(board)
print(empty_board())
    


# In[45]:


# check for empty places on tic-tac-toe board
def empty_places(board):
    l = []
    
    for i in range(len(board)):
     for j in range(len(board)):
        if board[i][j] == 0:
          l.append((i,j))
    return(l)

board = np.array([
                    [1,2,1],
                    [0,0,0],
                    [1,1,2]
                  ])
#print(empty_places(board))


# In[46]:


# Select a random place for the player on the Tic-Tac-Toe board.
def random_place(board, player):
    
   select = empty_places(board)
   current_location = random.choice(select)
   board[current_location] = player
   return(board)
print(random_place(board, 2))


# In[48]:


board = np.array([
                    [0,0,0],
                    [0,0,0],
                    [0,0,0]
                  ])
print(empty_places(board))
#check the horizontal rows for a winner

def row_winner():
    for x in range(len(board)):
        win = True
    
    for y in range(len(board)):
        if board[x,y] != player:
            win = False
            continue
    if win == True:
        return(win)
    return(win)
board = np.array([
                    [0,0,0],
                    [0,0,0],
                    [0,0,0]
])
#print(row_winner(board, 1))
    


# In[54]:


# Select a random place for the player on the Tic-Tac-Toe board.
def random_place(board, player):
    select = empty_places(board)
    current_location = random.choice(select)
    board[current_location] = player
    return(board)
print(random_place(board, 1))


# In[55]:


# Checks whether the player has three of their marks in a horizontal row
def row_winner(board, player):
    for x in range(len(board)):
        win = True
        for y in range(len(board)):
            if board[x, y] != player:
                win = False
                continue
                if win == True:
                    return(win)
        return(win)


# In[56]:


# Checks whether the player has three of their marks in a vertical row
def col_winner(board, player):
    for x in range(len(board)):
        win = True
        for y in range(len(board)):
            if board[y][x] != player:
                win = False
                continue
                if win == True:
                    return(win)
        return(win)


# In[62]:


# Check the diagnal rows for a winner
def diag_winner(board, player):
    win = True
    y = 0
    for x in range(len(board)):
        if board[x, x] != player:
            win = False
            if win:
                return win
            win = True
            if win:
                for x in range(len(board)):
                    y = len(board) - 1 - x
                    if board[x, y] != player:
                        win = False
                        return win
                    board = np.array([
                        [1,0,2],
                        [0,1,0],
                        [2,0,1]
                    ])
print(diag_winner(board,1))


# In[84]:


# Evaluates Whether there is a winner or a Tie
def evaluate_game(board):
# Winner [0 = indecisive; 1 = Player 1; 2 = Player 2; -1 = Tie]
    winner = 0
    for player in [1, 2]:
        if (row_winner(board, player) or
            col_winner(board, player) or
            diag_winner(board, player)):
             winner = player
    if np.all(board != 0) and winner == 0:
        winner = -1
    return winner


# In[95]:


def tic_tac_toe():
    board = empty_board()
    winner = 0
    counter = 1
    print(board)
    sleep(2)
    
    while winner == 0:
        for player in [1, 2]:
            brd = random_place(board, player)
            print("Board after " + str(counter) + " move")
            print(brd)
            sleep(2)
            counter += 3
            winner = evaluate_game(brd)
            
        if winner != 0:
            break
        return(winner)
print("Winner is player:" + str(tic_tac_toe()))


# In[97]:


import numpy as np
import random
from time import sleep
import matplotlib.pyplot as plt

def empty_board():
    return np.zeros((3, 3), dtype=int)

def random_place(board, player):
    selection = empty_indices(board)
    current_loc = random.choice(selection)
    board[current_loc] = player
    return board

def empty_indices(board):
    return list(zip(*np.where(board == 0)))

def evaluate_game(board):
    for player in [1, 2]:
        if any(np.all(board[row, :] == player) for row in range(3)):
            return player
        if any(np.all(board[:, col] == player) for col in range(3)):
            return player
        if np.all(np.diag(board) == player):
            return player
        if np.all(np.diag(np.fliplr(board)) == player):
            return player
    if not empty_indices(board):
        return -1  # Return -1 for a draw
    return 0

def display_board(board):
    plt.figure(figsize=(5, 5))
    plt.imshow(board, cmap='viridis', extent=(0, 3, 0, 3))
    plt.grid(True, which='both', color='black', linewidth=2)
    plt.xticks([0.5, 1.5, 2.5], ['', '', ''])
    plt.yticks([0.5, 1.5, 2.5], ['', '', ''])
    for (i, j), val in np.ndenumerate(board):
        if val == 1:
            plt.text(j + 0.5, 2.5 - i, 'X', ha='center', va='center', fontsize=48, color='white')
        elif val == 2:
            plt.text(j + 0.5, 2.5 - i, 'O', ha='center', va='center', fontsize=48, color='white')
    plt.show()

def tic_tac_toe():
    board = empty_board()
    winner = 0
    counter = 1
    display_board(board)
    sleep(2)
    
    while winner == 0:
        for player in [1, 2]:
            board = random_place(board, player)
            print("Board after " + str(counter) + " move")
            display_board(board)
            sleep(2)
            counter += 1
            winner = evaluate_game(board)
            
            if winner != 0:
                break
    
    return winner

print("Winner is player: " + str(tic_tac_toe()))


# In[ ]:




