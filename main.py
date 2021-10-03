import random


def getWords(wordList, maxLength, minLength):
    newList = []
    for i in wordList:
        if maxLength > len(i) > minLength:
            newList.append(i)

    word = newList[random.randrange(0, len(newList))]
    return word


def newGame(mode):
    themeList = ["animals", "gym", "computers"]
    themeIndex = random.randrange(0, len(themeList))
    theme = themeList[themeIndex]
    masterWordList = [["alligator", "zebra", "giraffe", "cat"],
                      ["dumbbell", "treadmill", "yoga"],
                      ["mouse", "gpu", "cpu", "case", "fan", "motherboard", "powersupply", "casefan", "button"]]

    if mode == 'easy':
        triesRemaining = 10
        maxWordLength = 5
        minWordLength = 0
        themedWord = getWords(masterWordList[themeIndex], maxWordLength, minWordLength)
        return triesRemaining, maxWordLength, minWordLength, theme, themedWord
    elif mode == 'medium':
        triesRemaining = 7
        maxWordLength = 10
        minWordLength = 5
        themedWord = getWords(masterWordList[themeIndex], maxWordLength, minWordLength)
        return triesRemaining, maxWordLength, minWordLength, theme, themedWord


def printUI(livesLeft, theme, word):
    print("Lives left: {}     Theme: {}\n{}".format(livesLeft, theme, word))


def findOccurrences(s, ch):
    return [i for i, letter in enumerate(s) if letter == ch]


def playerGuess(letter, completeWord, emptyWord):
    emptyWord = list(emptyWord)  # Must convert str->list so that it can be modified
    if letter in completeWord:
        letterIndices = findOccurrences(completeWord, letter)
        for i in letterIndices:
            emptyWord[i] = letter
    else:
        return "none"

    emptyWord = "".join(emptyWord)  # Convert back to string
    return emptyWord

# Main Function
def main():
    livesRemaining, maxLetterCount, minLetterCount, theme, themedWord = newGame('medium')

    blankWord = "_" * len(themedWord)

    while livesRemaining != 0:
        if blankWord == themedWord:
            printUI(livesRemaining, theme, blankWord)
            print("You Win!!!!!!!")
            break
        printUI(livesRemaining, theme, blankWord)
        guess = input("What's your guess?")
        if playerGuess(guess, themedWord, blankWord) != "none":
            blankWord = playerGuess(guess, themedWord, blankWord)
        else:
            livesRemaining -= 1
    if livesRemaining == 0:
        print("Try again! The word was: {}".format(themedWord))


if __name__ == '__main__':
    main()
