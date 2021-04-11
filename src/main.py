from logic.calc import Process
from data.db import Database


data = Database()
script1 = Process(data)
script1.print()
