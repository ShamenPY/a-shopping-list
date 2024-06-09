import time
from tkinter import *
class App:
    def __init__(self):
        self.main()

    def window(self):
        #creating window in tkinter
        self.root = Tk()


        self.root.title("a shopping list")
        self.root.configure(background="white")
        self.root.minsize(200, 200)  
        self.root.maxsize(500, 500)
        self.root.geometry("300x300+50+50")
        text = Label(self.root,text="Welcome to a shopping list :) ")
        text.pack()

        add_b = Button(self.root, text="Click to add new list", command=self.add_b)
        add_b.pack(side="left")
        self.root.mainloop()



    def add_b(self):
        print("dd")
        root = Tk()

        root.minsize(200, 200)
        root.maxsize(500, 500)
        root.title("ADDING A NEW LIST")

        root.mainloop()
    def main(self):
        self.window()

App = App()
