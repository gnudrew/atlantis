# Implement a GUI:
# Object Oriented approach, defining GuessingGUI class

from tkinter import *
import numpy as np
r = np.random.randint

class GuessingGUI:
    def __init__(self, master):
        self.master = master
        master.title("Number Guessing Game")

        self.guess = StringVar() #user guess
        self.entry_field = Entry(master,textvariable=self.guess)
        self.entry_field.pack()

        self.guess_button = Button(master,text='Guess',command=self.check)
        self.guess_button.pack()

        self.randGen_button = Button(master,text='new number',command=self.genrand)
        self.randGen_button.pack()

        self.text_field = Text(master)
        self.text_field.pack()

        self.exit_button = Button(master,text='Exit',command=master.quit)
        self.exit_button.pack()

        self.genrand() #holds the randomly generated int

    def genrand(self,):
        self.rand = r(1,100+1)
        # print("new random number is: "+str(self.rand))
        self.text_field.insert(END,"New number generated--take a guess.\n")

    def check(self,):
        a = int(self.rand) #the current random number
        b = int(self.guess.get()) #the current guess, read from entry field
        # print("rand is "+str(a)+". guess is "+str(b)+".")
        if a == b:
            self.gotIt()
        elif a < b:
            self.text_field.insert(END,"Nope, lower.\n")
        elif a > b:
            self.text_field.insert(END,"Nope, higher.\n")
    
    def gotIt(self,):
        self.text_field.insert(END,"Yup!\n")
        self.text_field.insert(END,"░░░░░░░░░░░░░░░░░░░░░░█████████\n")
        self.text_field.insert(END,"░░███████░░░░░░░░░░███▒▒▒▒▒▒▒▒███\n")
        self.text_field.insert(END,"░░█▒▒▒▒▒▒█░░░░░░░███▒▒▒▒▒▒▒▒▒▒▒▒▒███\n")
        self.text_field.insert(END,"░░░█▒▒▒▒▒▒█░░░░██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██\n")
        self.text_field.insert(END,"░░░░█▒▒▒▒▒█░░░██▒▒▒▒▒██▒▒▒▒▒▒██▒▒▒▒▒███\n")
        self.text_field.insert(END,"░░░░░█▒▒▒█░░░█▒▒▒▒▒▒████▒▒▒▒████▒▒▒▒▒▒██\n")
        self.text_field.insert(END,"░░░█████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██\n")
        self.text_field.insert(END,"░░░█▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒██\n")
        self.text_field.insert(END,"░██▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒██▒▒▒▒▒▒▒▒▒▒██▒▒▒▒██\n")
        self.text_field.insert(END,"██▒▒▒███████████▒▒▒▒▒██▒▒▒▒▒▒▒▒██▒▒▒▒▒██\n")
        self.text_field.insert(END,"█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒████████▒▒▒▒▒▒▒██\n")
        self.text_field.insert(END,"██▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██\n")
        self.text_field.insert(END,"░█▒▒▒███████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██\n")
        self.text_field.insert(END,"░██▒▒▒▒▒▒▒▒▒▒████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█\n")
        self.text_field.insert(END,"░░████████████░░░█████████████████\n")

game = Tk()
my_game = GuessingGUI(game)
game.mainloop()