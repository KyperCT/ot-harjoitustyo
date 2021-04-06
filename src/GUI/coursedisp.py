from tkinter.ttk import Treeview
from tkinter import Frame


class CourseTree(Frame):
    def __init__(self, master):
        super(CourseTree, self).__init__()
        tree = Treeview(master)

        tree.pack()