import sys
import random
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from mainwindow import Ui_MainWindow
from sudoku import Sudoku
from functools import partial

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.menu_new.triggered.connect(self.new_game)
        self.ui.menu_openfile.triggered.connect(self.open_file)
        self.line_edits = [[None for i in range(9)] for j in range(9)]

        self.new_game()

    def new_game(self):
        global puzzle
        puzzle = Sudoku(3, seed=random.randint(1, 1000)).difficulty(0.5)
        for i in range(9):
            for j in range(9):

                new_cell = QLineEdit()
                self.ui.grid_layout.addWidget(new_cell, i, j)
                new_cell.textChanged.connect(partial(self.validation, i, j))
                self.line_edits[i][j] = new_cell
                self.line_edits[i][j].setReadOnly(False)
                new_cell.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.MinimumExpanding)
                new_cell.setAlignment(Qt.AlignHCenter)

                if puzzle.board[i][j] != None:
                    self.line_edits[i][j].setText(str(puzzle.board[i][j]))
                    self.line_edits[i][j].setReadOnly(True)
                else:
                    self.line_edits[i][j].setText("")
                

    def open_file(self):
        try: 
            file_path = QFileDialog.getOpenFileName(self, "Open File...")[0]
            f = open(file_path, "r")
            big_text = f.read()
            rows = big_text.split("\n")
            puzzle_board = [[None for i in range(9)] for j in range(9)]
            for i in range(len(rows)):
                cells = rows[i].split(" ")
                for j in range(len(cells)):
                    puzzle_board[i][j] = int(cells[j])
            
            for i in range(9):
                for j in range(9):
                    if puzzle_board[i][j] != 0:
                        self.line_edits[i][j].setText(str(puzzle_board[i][j]))
                        self.line_edits[i][j].setReadOnly(True)
                    else:
                        self.line_edits[i][j].setText("")   
        except:
            msg = QMessageBox()
            msg.setText('An error occurred!')
            msg.exec()             

    def check(self, i, j, text):
        
        for i1 in range(0, 9):
            for j1 in range(0, 9):
                num = self.line_edits[i1][j1].text()
                if num == text and i == i1 and j != j1:
                    self.line_edits[i][j].setStyleSheet("background-color: #ff909b")
        
        for i2 in range(0, 9):
            for j2 in range(0, 9):
                num = self.line_edits[i2][j2].text()
                if num == text and i != i2 and j == j2:
                    self.line_edits[i][j].setStyleSheet("background-color: #ff909b")   

        if 0 <= i < 3 and 0 <= j < 3 :
            for i3 in range(0, 3):
                for j3 in range(0, 3):
                    num = self.line_edits[i3][j3].text()
                    if num == text and i != i3 and j != j3:
                        self.line_edits[i][j].setStyleSheet("background-color: #ff909b")   

        if 0 <= i < 3 and 3 <= j < 6 :
            for i4 in range(0, 3):
                for j4 in range(3, 6):
                    num = self.line_edits[i4][j4].text()
                    if num == text and i != i4 and j != j4:
                        self.line_edits[i][j].setStyleSheet("background-color: #ff909b;")   

        if 0 <= i < 3 and 6 <= j < 9 :
            for i5 in range(0, 3):
                for j5 in range(6, 9):
                    num = self.line_edits[i5][j5].text()
                    if num == text and i != i5 and j != j5:
                        self.line_edits[i][j].setStyleSheet("background-color: #ff909b;")   

        if 3 <= i < 6 and 0 <= j < 3 :
            for i6 in range(3, 6):
                for j6 in range(0, 3):
                    num = self.line_edits[i6][j6].text()
                    if num == text and i != i6 and j != j6:
                        self.line_edits[i][j].setStyleSheet("background-color: #ff909b;")   

        if 3 <= i < 6 and 3 <= j < 6 :
            for i7 in range(3, 6):
                for j7 in range(3, 6):
                    num = self.line_edits[i7][j7].text()
                    if num == text and i != i7 and j != j7:
                        self.line_edits[i][j].setStyleSheet("background-color: #ff909b;")

        if 3 <= i < 6 and 6 <= j < 9 :
            for i8 in range(3, 6):
                for j8 in range(6, 9):
                    num = self.line_edits[i8][j8].text()
                    if num == text and i != i8 and j != j8:
                        self.line_edits[i][j].setStyleSheet("background-color: #ff909b;")
        
        if 6 <= i < 9 and 0 <= j < 3 :
            for i9 in range(6, 9):
                for j9 in range(0, 3):
                    num = self.line_edits[i9][j9].text()
                    if num == text and i != i9 and j != j9:
                        self.line_edits[i][j].setStyleSheet("background-color: #ff909b;")
        
        if 6 <= i < 9 and 3 <= j < 6 :
            for i10 in range(6, 9):
                for j10 in range(3, 6):
                    num = self.line_edits[i10][j10].text()
                    if num == text and i != i10 and j != j10:
                        self.line_edits[i][j].setStyleSheet("background-color: #ff909b;")  

        if 6 <= i < 9 and 6 <= j < 9 :
            for i11 in range(6, 9):
                for j11 in range(6, 9):
                    num = self.line_edits[i11][j11].text()
                    if num == text and i != i11 and j != j11:
                        self.line_edits[i][j].setStyleSheet("background-color: #ff909b;")

    # def check_win(self):
    #     puzzle_board = [[None for i in range(9)] for j in range(9)]
    #     answer_board = [[None for i in range(9)] for j in range(9)]
    #     answer = self.puzzle.solve()
    #     for ii in range(9):
    #         for jj in range(9):
    #             puzzle_board[ii][jj] = self.line_edits[ii][jj].text()
    #             answer_board[ii][jj] = str(answer[ii][jj])

    #     if puzzle_board == answer_board:
    #         print("*** You Win! ***")
    #         msg = QMessageBox()
    #         msg.setText('*** You Win! ***')
    #         msg.exec()

    def validation(self, i, j, text):
        if text not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            self.line_edits[i][j].setText("")

        self.check(i, j, text)
        self.check_win()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()