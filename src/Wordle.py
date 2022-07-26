from tkinter import *
import random, json, re

class Wordle: 
    def __init__(self, root):
        self.tklabels, self.helper, self.tkbuttons, self.guesses = [], [], [], []
        self.unusedLetters = []
        self.root = root
        self.index = 0
        self.restartBool = False
        self.currentAttempt = 0
        self.randomWord = None
        buttonQ = Button(self.root, text = 'Q', font = 'Sans-Serif 15 bold', fg = 'white', bg = 'black', width = 2, height = 1, command = lambda: Wordle.onClick(self, 0))
        buttonW = Button(self.root, text = 'W', font = 'Sans-Serif 15 bold', fg = 'white', bg = 'black', width = 2, height = 1, command = lambda: Wordle.onClick(self, 1))
        buttonE = Button(self.root, text = 'E', font = 'Sans-Serif 15 bold', fg = 'white', bg = 'black', width = 2, height = 1, command = lambda: Wordle.onClick(self, 2))
        buttonR = Button(self.root, text = 'R', font = 'Sans-Serif 15 bold', fg = 'white', bg = 'black', width = 2, height = 1, command = lambda: Wordle.onClick(self, 3))
        buttonT = Button(self.root, text = 'T', font = 'Sans-Serif 15 bold', fg = 'white', bg = 'black', width = 2, height = 1, command = lambda: Wordle.onClick(self, 4))
        buttonY = Button(self.root, text = 'Y', font = 'Sans-Serif 15 bold', fg = 'white', bg = 'black', width = 2, height = 1, command = lambda: Wordle.onClick(self, 5))
        buttonU = Button(self.root, text = 'U', font = 'Sans-Serif 15 bold', fg = 'white', bg = 'black', width = 2, height = 1, command = lambda: Wordle.onClick(self, 6))
        buttonI = Button(self.root, text = 'I', font = 'Sans-Serif 15 bold', fg = 'white', bg = 'black', width = 2, height = 1, command = lambda: Wordle.onClick(self, 7))
        buttonO = Button(self.root, text = 'O', font = 'Sans-Serif 15 bold', fg = 'white', bg = 'black', width = 2, height = 1, command = lambda: Wordle.onClick(self, 8))
        buttonP = Button(self.root, text = 'P', font = 'Sans-Serif 15 bold', fg = 'white', bg = 'black', width = 2, height = 1, command = lambda: Wordle.onClick(self, 9))
        buttonA = Button(self.root, text = 'A', font = 'Sans-Serif 15 bold', fg = 'white', bg = 'black', width = 2, height = 1, command = lambda: Wordle.onClick(self, 10))
        buttonS = Button(self.root, text = 'S', font = 'Sans-Serif 15 bold', fg = 'white', bg = 'black', width = 2, height = 1, command = lambda: Wordle.onClick(self, 11))
        buttonD = Button(self.root, text = 'D', font = 'Sans-Serif 15 bold', fg = 'white', bg = 'black', width = 2, height = 1, command = lambda: Wordle.onClick(self, 12))
        buttonF = Button(self.root, text = 'F', font = 'Sans-Serif 15 bold', fg = 'white', bg = 'black', width = 2, height = 1, command = lambda: Wordle.onClick(self, 13))
        buttonG = Button(self.root, text = 'G', font = 'Sans-Serif 15 bold', fg = 'white', bg = 'black', width = 2, height = 1, command = lambda: Wordle.onClick(self, 14))
        buttonH = Button(self.root, text = 'H', font = 'Sans-Serif 15 bold', fg = 'white', bg = 'black', width = 2, height = 1, command = lambda: Wordle.onClick(self, 15))
        buttonJ = Button(self.root, text = 'J', font = 'Sans-Serif 15 bold', fg = 'white', bg = 'black', width = 2, height = 1, command = lambda: Wordle.onClick(self, 16))
        buttonK = Button(self.root, text = 'K', font = 'Sans-Serif 15 bold', fg = 'white', bg = 'black', width = 2, height = 1, command = lambda: Wordle.onClick(self, 17))
        buttonL = Button(self.root, text = 'L', font = 'Sans-Serif 15 bold', fg = 'white', bg = 'black', width = 2, height = 1, command = lambda: Wordle.onClick(self, 18))
        buttonZ = Button(self.root, text = 'Z', font = 'Sans-Serif 15 bold', fg = 'white', bg = 'black', width = 2, height = 1, command = lambda: Wordle.onClick(self, 19))
        buttonX = Button(self.root, text = 'X', font = 'Sans-Serif 15 bold', fg = 'white', bg = 'black', width = 2, height = 1, command = lambda: Wordle.onClick(self, 20))
        buttonC = Button(self.root, text = 'C', font = 'Sans-Serif 15 bold', fg = 'white', bg = 'black', width = 2, height = 1, command = lambda: Wordle.onClick(self, 21))
        buttonV = Button(self.root, text = 'V', font = 'Sans-Serif 15 bold', fg = 'white', bg = 'black', width = 2, height = 1, command = lambda: Wordle.onClick(self, 22))
        buttonB = Button(self.root, text = 'B', font = 'Sans-Serif 15 bold', fg = 'white', bg = 'black', width = 2, height = 1, command = lambda: Wordle.onClick(self, 23))
        buttonN = Button(self.root, text = 'N', font = 'Sans-Serif 15 bold', fg = 'white', bg = 'black', width = 2, height = 1, command = lambda: Wordle.onClick(self, 24))
        buttonM = Button(self.root, text = 'M', font = 'Sans-Serif 15 bold', fg = 'white', bg = 'black', width = 2, height = 1, command = lambda: Wordle.onClick(self, 25))
        self.buttons = [buttonQ,buttonW,buttonE,buttonR,buttonT,buttonY,buttonU,buttonI,buttonO,buttonP,buttonA,buttonS,buttonD,buttonF,buttonG,buttonH,buttonJ,buttonK,buttonL,buttonZ,buttonX,buttonC,buttonV,buttonB,buttonN,buttonM]
        self.relx, self.rely = [.3, .4, .5, .6, .7], [.05, .15, .25, .35, .45, .55] 

    def setRandomWord(self):
        with open('Wordle2\src\words.json') as words:
            words = json.load(words)['Words']
            length = len(words)
            word = words[random.randint(0, length)].upper()
        self.word = word
        print(self.word)

    def check(self):
        colors = []
        guessString = "".join([i for i in self.guesses[self.currentAttempt]])
        for i in guessString:
            wordIndexes = []
            guessIndexes = []
            if i in self.word:
                wordIndexes = [i.start() for i in re.finditer(i, self.word)]
                guessIndexes = [i.start() for i in re.finditer(i, guessString)]
                for j in range(len(wordIndexes)):
                    if wordIndexes == guessIndexes:
                        colors.append("green")
                        self.buttons[self.qwerty.index(i)].config(bg = 'green')
                    else:
                        colors.append("yellow")
                        self.buttons[self.qwerty.index(i)].config(bg = 'yellow')
            else:
                colors.append("white")
                self.unusedLetters.append(i)
                self.unusedLetters = list(set(self.unusedLetters))

        for index, i in enumerate(self.tklabels[self.currentAttempt]):
            i[0].config(fg = colors[index])


        if len([i for i in colors if i == 'green']) == 5:
            winLabel = Label(self.root, text=f'You got it!', font = 'Sans-Serif 15 bold', fg = 'white', bg = 'black')
            winLabel.place(relx = .5, rely = .02, anchor = N)
            Wordle.endGame(self)

        colors.clear()
        self.currentAttempt += 1
        self.index = 0

        if self.currentAttempt > 5:
            Wordle.endGame(self)
            lossLabel = Label(self.root, text = f'{self.word}', font = 'Sans-Serif 15 bold', fg = 'white', bg = 'black')
            lossLabel.place(relx = .5, rely = .02, anchor = N)

        for letter in self.unusedLetters:
            self.buttons[self.qwerty.index(letter)].config(fg = 'grey45')

    def endGame(self):
        for i in self.buttons:
            i['state'] = 'disabled'
        self.helper[0]['state'] = 'disabled'
        self.helper[1]['state'] = 'disabled'

    def setAndGetLabels(self):
        for i in range(6):
            labels = []
            for k in range(5):
                labels.append([Label(self.root, text = f"{'_' * 2}",font = "Sans-Serif 25 bold", fg = 'white', bg = 'black', padx = 22, pady = 20), self.relx[k], self.rely[i]])
            self.tklabels.append(labels)
        return self.tklabels 
    
    def onClick(self, index):
        Wordle.enterLetters(self, letter = self.qwerty[index])

    def enterLetters(self, letter):
        if self.index <= 4 and self.currentAttempt <= 5:
            self.tklabels[self.currentAttempt][self.index][0].config(text = letter)
            self.index += 1

    def delLetters(self):
        if self.index != 0 and self.currentAttempt <= 5:
            self.index -= 1
            self.tklabels[self.currentAttempt][self.index][0].config(text = "__")\
    
    def submitButton(self):
        if self.index == 5:
            self.guess = []
            for i in self.tklabels[self.currentAttempt]:
                self.guess.append(i[0].cget('text'))
            self.guesses.append(self.guess)
            Wordle.check(self)

    def setAndGetButtons(self):
        self.qwerty = 'QWERTYUIOPASDFGHJKLZXCVBNM'
        offsetX = .05
        yPos = .75
        xPos = .1
        for index, value in enumerate(self.qwerty):
            if value == 'H':
                yPos = .85
                xPos = .2
                offsetX = .05
            self.tkbuttons.append([self.buttons[index], round(xPos + offsetX, 2), round(yPos, 2)])
            offsetX += .05

        enterButton = Button(self.root, text = "ENTER", font = "Sans-Serif 15 bold", fg = 'white', bg = 'black',
        width = 6, height = 1, command = lambda: Wordle.submitButton(self))
        delButton = Button(self.root, text = "DEL", font = "Sans-Serif 15 bold", fg = 'white', bg = 'black', 
        width = 3, height = 1, command = lambda: Wordle.delLetters(self))

        self.helper.append(enterButton)
        self.helper.append(delButton)  

        enterButton.place(relx = .16, rely = .85, anchor = N)
        delButton.place(relx = .81, rely = .85, anchor = N)

        return self.tkbuttons
        
    def placeButtons(self):
        for i in self.tkbuttons: 
            i[0].place(relx = i[1], rely = i[2], anchor = N)

    def placeLabels(self):
        counter = 0
        for i in self.tklabels:
            for j in range(5):
                self.tklabels[counter][j][0].place(relx = self.tklabels[counter][j][1], 
                rely = self.tklabels[counter][j][2], anchor = N)
            counter += 1