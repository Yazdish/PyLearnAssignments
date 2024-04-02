import sys
import random
from functools import partial
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import *

score_player = 0
score_cpu = 0

def play(player_choice):
    
    if player_choice == 1:
        main_window.player_board.setText("✊")
    elif player_choice == 2:
        main_window.player_board.setText("🖐")
    elif player_choice == 3:
        main_window.player_board.setText("✌")

    cpu_play()
    check(player_choice, cpu_choice)

def cpu_play():

    global cpu_choice
    cpu_choice = random.randint(1,3)
    if cpu_choice == 1:
        main_window.cpu_board.setText("✊")
    elif cpu_choice == 2:
        main_window.cpu_board.setText("🖐")
    elif cpu_choice == 3:
        main_window.cpu_board.setText("✌")

def check(player_choice, cpu_choice):
    global score_player
    global score_cpu
    
    if player_choice == 1 and cpu_choice == 3 or player_choice == 2 and cpu_choice == 1 or \
    player_choice == 3 and cpu_choice == 2:
        score_player += 1
        main_window.score_player.setText(str(score_player))
        main_window.result_board.setText("You Win!")
    elif player_choice == 3 and cpu_choice == 1 or player_choice == 1 and cpu_choice == 2 or \
    player_choice == 2 and cpu_choice == 3:
        score_cpu += 1
        main_window.score_cpu.setText(str(score_cpu))
        main_window.result_board.setText("Computer Wins!")
    else:
        main_window.result_board.setText("Tied!")


loader = QUiLoader()
app = QApplication(sys.argv)

main_window = loader.load("main_window.ui")
main_window.setWindowTitle("Rock Paper Scissors")
main_window.show()

main_window.score_player.setText(str(score_player))
main_window.score_cpu.setText(str(score_cpu))
main_window.result_board.setText("start")

main_window.btn_rock.setText("✊")
main_window.btn_paper.setText("🖐")
main_window.btn_scissors.setText("✌")

main_window.btn_rock.clicked.connect(partial(play, 1))
main_window.btn_paper.clicked.connect(partial(play, 2))
main_window.btn_scissors.clicked.connect(partial(play, 3))

app.exec()