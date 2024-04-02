import pyfiglet
from termcolor import colored
import time
import random

Winner = None

def Menu():
   print("Player vs Player Enter: 1")
   print("Player vs CPU Enter: 2")
   choice=int(input("your choice: "))
   return choice


def show():
    for row in game_board:
        for cell in row:
            print(cell, end=" ")
        print()

def check_game():
    for i in range(3):
        if game_board[i][0] == game_board[i][1] == game_board[i][2] == "X" or game_board[0][i] == game_board[1][i] == game_board[2][i] == "X":
            print("player1 wins!")
            Winner != None
        
        if game_board[i][0] == game_board[i][1] == game_board[i][2] == "O" or game_board[0][i] == game_board[1][i] == game_board[2][i] == "O":
            print("player1 lost!")
            Winner != None

    if game_board[0][0] == game_board[1][1] == game_board[2][2] == "X" or game_board[0][2] == game_board[1][1] == game_board[2][0] == "X":
        print("player1 wins!")
        Winner != None

    if game_board[0][0] == game_board[1][1] == game_board[2][2] == "O" or game_board[0][2] == game_board[1][1] == game_board[2][0] == "O":
        print("player1 lost!")
        Winner != None
        
    for i in range(3):
        for j in range(3):
            if game_board[i][j] is None:
                return None

    return "Draws"
    
title = pyfiglet.figlet_format("TICTACTOE", font="slant")

print(title)

game_board = [["-","-","-"]
            ,["-","-","-"]
            ,["-","-","-"]]

show()
start_time = time.time()
choice = Menu()
if choice == 1:
    while Winner == None:
        while True:
            print("player1")
            row = int(input("row: "))
            col = int(input("col: "))
            
            if 0 <= row <= 2 and 0 <= col <= 2:
                if game_board[row][col] == "-":
                    game_board[row][col] = colored("X",'red')
                    break
                else:
                    print(":/")
            else:
                print(":???")    
        show()
        check_game()
        while True:    
            print("player2")
            row = int(input("row: "))
            col = int(input("col: "))
            
            if 0 <= row <= 2 and 0 <= col <= 2:
                if game_board[row][col] == "-":
                    game_board[row][col] = colored("O",'blue')
                    break
                else:
                    print(":/")
            else:
                print(":???")
        show()
        check_game()

elif choice == 2:
    while Winner == None:
        while True:
            print("player1")
            row = int(input("row: "))
            col = int(input("col: "))
            
            if 0 <= row <= 2 and 0 <= col <= 2:
                if game_board[row][col] == "-":
                    game_board[row][col] = colored("X",'red')
                    break
                else:
                    print(":/")
            else:
                print(":???")    
        show()
        check_game()
        while True:
            print("CPU")
            row=random.randint(0,2)
            col=random.randint(0,2)

            if game_board[row][col]=="-":
                game_board[row][col]=colored("O",'blue')
                break
        show()
        check_game()        
    
    
    
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Elapsed time: ", elapsed_time) 

