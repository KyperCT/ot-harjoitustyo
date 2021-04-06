import calc
import db


data = db.Database()
script1 = calc.Process(data)
script1.print()
