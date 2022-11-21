secretWord = 'DEVELOPER'
guesses = []
estimate_of_guesses = 0

wordBoard = []
for letter in range(len(secretWord)):
    wordBoard.append('_')

def showBoard():
    print(' '.join(wordBoard))

def checkGuess(lett):
    lett = lett.upper()
    index = secretWord.find(lett)
    
    if(index > -1):
        indices = [i for i in range(len(secretWord)) if secretWord[i] == lett]
        for i in indices:
            wordBoard[i] = lett
        if (secretWord.count(lett) > 1):
            print(f"Yes there are {secretWord.count(lett)} {lett} ")
        else:
            print(f"Yes there is a {lett}")
        guesses.append(lett)
        return True
    else:
        print(f"Im sorry but there is no letter {lett} in the word")
        guesses.append(lett)
        return False

def split(word):
    return [char for char in word]

def wordGuess():
    print("Can you guess the secret occupation?")
    showBoard()
    global estimate_of_guesses
    while(estimate_of_guesses < 5):
        guessLetter = input("Guess a letter: ").upper()
        
        while(guessLetter in guesses):
            guessLetter = input("Guess another letter: ")
        if (checkGuess(guessLetter)):
            showBoard()
            if (not '_' in wordBoard):
                print("You Won!")
                break
        else:
            estimate_of_guesses += 1
            print(f"You have {5 - estimate_of_guesses} chances left")
            showBoard()
            if(estimate_of_guesses > 4):
                print(f"You lose. The secret word was...{secretWord}")

wordGuess()
