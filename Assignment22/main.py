import sys
from functools import partial
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from mainwindow import Ui_MainWindow
from database import Database

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.db = Database()
        self.read_from_database()
        self.ui.btn_new_task.clicked.connect(self.new_task)
        

    def new_task(self):
        new_title = self.ui.tb_new_task_title.text()
        new_description = self.ui.tb_new_task_description.toPlainText()
        priority = self.ui.priority.currentText()
        new_date_time = self.ui.dateTime.text()

        feedback = self.db.add_new_task(new_title, new_description, priority, new_date_time)
        
        if feedback == True:
            self.read_from_database()
            self.ui.tb_new_task_title.setText("")
            self.ui.tb_new_task_description.setPlainText("")
            self.ui.priority.currentText("Low")
            
        else:
            msg_box = QMessageBox()
            msg_box.setText("something wrong")
            msg_box.exec_()

    def show_description(self, task, x):
        details = f"description:\n  {task[2]}\ndate and time:\n  {task[5]}"
        msg_box = QMessageBox()
        msg_box.setWindowTitle(f"task: {task[1]}")
        msg_box.setText(details)
        msg_box.exec()

    def read_from_database(self):
        global id
        tasks = self.db.get_tasks()

        for i in range(len(tasks)):
            id = tasks[i][0]
            new_checkbox = QCheckBox()
            new_label = QLabel()
            del_btn = QPushButton()
            priority_btn = QPushButton()

            new_label.setText(tasks[i][1])
            # new_label.setStyleSheet("background-color: orange")
            del_btn.setText("Delete")
            
            if tasks[i][4] == "Low":
                priority_btn.setText("Low")
                priority_btn.setStyleSheet("background-color: #08cf79; border-radius: 5px ")
            elif tasks[i][4] == "Medium":
                priority_btn.setText("Medium")
                priority_btn.setStyleSheet("background-color: #fac105; border-radius: 5px ")
            elif tasks[i][4] == "High":
                priority_btn.setText("High")
                priority_btn.setStyleSheet("background-color: #db1414; border-radius: 5px")

            if tasks[i][3] == 1:
                new_checkbox.setChecked(True)
                new_label.setStyleSheet("text-decoration:line-through")
            elif tasks[i][3] == 0:
                new_checkbox.setChecked(False)
            
            self.ui.gl_tasks.addWidget(del_btn, i, 2)
            self.ui.gl_tasks.addWidget(new_checkbox, i, 0)
            self.ui.gl_tasks.addWidget(new_label, i, 1)
            self.ui.gl_tasks.addWidget(priority_btn, i, 3)
            del_btn.clicked.connect(partial(self.db.remove_task, id))
            new_checkbox.clicked.connect(partial(self.db.task_status, id))
            new_label.mousePressEvent=partial(self.show_description, tasks[i])

if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()
    app.exec()