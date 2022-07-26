from colorama import Fore, Style
import json, random, re

with open('Wordle2\src\words.json') as words:
    words = json.load(words)['Words']
    length = len(words)
    word = words[random.randint(0, length)].upper()


print(f'┌{"─" * 15}┐')

for i in range(6):
    print('│', end = '')
    print(" _ " * 5, end = '')
    print('│')

print(f'└{"─" * 15}┘')
unusedLetters, guesses = [], []
win, valid = False, True
currentGuessCount = 0
while currentGuessCount != 6: 
    string = ""
    correctCount = 0
    guess = input("Enter A Word: ").upper()
    if len(guess) == 5:
        valid = True
        for i in guess:
            wordIndexes = []
            guessIndexes = []
            if i in word:
                wordIndexes = [i.start() for i in re.finditer(i, word)]
                guessIndexes = [i.start() for i in re.finditer(i, guess)]
                for j in range(len(wordIndexes)):
                    if wordIndexes == guessIndexes:
                        correctCount += 1
                        string += (f' {Style.BRIGHT + Fore.GREEN + i + Fore.WHITE + Style.RESET_ALL} ')
                    else:
                        string += (f' {Style.BRIGHT + Fore.YELLOW + i + Fore.WHITE + Style.RESET_ALL} ') 
            else:
                string += (f' {i} ')
                unusedLetters.append(i)
                unusedLetters = list(set(unusedLetters))
                unusedLetters.sort()
        currentGuessCount += 1
    else:
        print("Invalid Input")
        valid = False

    if valid:
        guesses.append(string)

    print(f'┌{"─" * 15}┐')

    for i in guesses:
        print('│', end = '')
        print(f'{i}', end = '')
        print('│')

    for i in range(6 - currentGuessCount):
        print('│', end = '')
        print(" _ " * 5, end = '')
        print('│')

    print(f'└{"─" * 15}┘')

    print(f'Letters That Are Not in the Word: ', end = '')
    print(''.join([i for i in unusedLetters]))

    if correctCount == 5:
        print(Fore.GREEN +'  C O R R E C T' + Fore.WHITE)
        break

print(f"THE WORD WAS {word}")


