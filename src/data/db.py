import sqlite3
from os import path


class Database:
    def __init__(self):
        if path.isfile("ex.db"):
            self.db = sqlite3.connect("ex.db")
            self.cur = self.db.cursor()
        else:
            self.db = sqlite3.connect("ex.db")
            self.cur = self.db.cursor()
            self.setup()

    def setup(self):
        self.cur.execute("CREATE TABLE courses (id INTEGER PRIMARY KEY, name TEXT, points INTEGER)")
        self.db.commit()

    def insertcourse(self, data: dict):
        dat = (data['name'], data['points'])
        self.cur.execute("INSERT INTO courses (name, points) VALUES (?, ?)", dat)
        self.db.commit()

    def getcourses(self):
        return self.cur.execute("SELECT * FROM courses").fetchall()
