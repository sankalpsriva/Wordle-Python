from tkinter import *
from Wordle import Wordle

def main():
    root = Tk() 
    root.geometry('700x900') 
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

if __name__ == '__main__':
    main()
    
