from tkinter import *
from Wordle import Wordle
from string import ascii_lowercase as lower

root = Tk() 
root.geometry('700x850') 
root.title('Wordle')
root.config(bg = 'black')

wordle = Wordle(root)

wordle.setAndGetLabels()
wordle.setAndGetButtons()
wordle.setRandomWord()
wordle.placeLabels()
wordle.placeButtons()

root.iconphoto(False, PhotoImage(file='Wordle2\src\download.png'))

root.mainloop() 
    
