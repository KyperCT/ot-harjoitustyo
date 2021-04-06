from tkinter import Tk, Frame
from coursedisp import CourseTree
root = Tk()


class GUI(Frame):
    def __init__(self, master):
        super(GUI, self).__init__()
        mainframe = Frame(master)
        tree1 = CourseTree(mainframe)

        tree1.grid()
        mainframe.grid()


GUI(root).grid()
root.mainloop()
