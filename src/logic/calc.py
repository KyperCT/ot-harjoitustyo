

class Process:
    def __init__(self, db):
        self.db = db

    def print(self):
        """This is a test function, it will be removed in time"""
        self.db.insertcourse({"name": "Ohja", "points": 5})
        print(self.db.getcourses())