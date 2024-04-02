import sqlite3

class Database:
    def __init__(self):
        self.con = sqlite3.connect("todo_list.db")
        self.cursor =self.con.cursor()

    def get_tasks(self):
        query = "SELECT * FROM tasks"
        result = self.cursor.execute(query)
        tasks = result.fetchall()
        return tasks
    
    def add_new_task(self, new_title, new_description, priority, new_date_time):
        try:
            query = f"INSERT INTO tasks (title, description, priority, dateTime) VALUES ('{new_title}', '{new_description}', '{priority}', '{new_date_time}')"
            self.cursor.execute(query)
            self.con.commit()
            return True
        except:
            return False
        
    def remove_task(self, id):
        try :
            query = f"DELETE FROM tasks WHERE id = {id}"
            self.cursor.execute (query)
            self.con.commit ()
            return True
        
        except :
            return False

    def task_status(self, id):
        status = 1
        query = f"UPDATE tasks SET status = '{status}' WHERE id='{id}'"  
        self.cursor.execute(query)
        self.con.commit()
