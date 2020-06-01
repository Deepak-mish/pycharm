from tkinter import *


class login_system:
    def __init__(self, root):
        self.root = root
        self.root.title("login system")
        self.root.geometry("1300x700+0+0")


root = Tk()
obj = login_system(root)
root.mainloop()
