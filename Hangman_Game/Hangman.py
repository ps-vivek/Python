#
#Hangman game
#GAME RULES:
#Computer randomly picks a word. A user is given 8 tries to guess the word.
#For every incorrect try a guess is subtracted
#
import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    count=0
    # FILL IN YOUR CODE HERE...
    l_secretword=len(secretWord)
    for i in secretWord:
        if i in lettersGuessed:
            count+=1

    if(count == len(secretWord)):
        return True
    else:
        return False



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    s_w_l=len(secretWord) # finding the len of secret word and appending the ans as an empty list with all contents as underscores
    ans=[]
    for i in range(len(secretWord)):
        ans.append(' _ ')

    lg=[] #list to remove multiple occurences of a letter
    for i in lettersGuessed:
        if not i in lg:
            lg.append(i)
    l_index=[]
    # FILL IN YOUR CODE HERE...
    for letter in lg: #finding the indexes of letters (multiple letters are even accounted for)
        index=0

        i=secretWord.find(letter,index)
        #print letter,i
        while (i>=0):

            l_index.append([letter,i])
            i=secretWord.find(letter,i+1)
        #print l_index

    for i in l_index: #substituting the underscores in the ans list with the found letter
        ans[i[1]]=i[0]


    return ''.join(ans)


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    a=string.lowercase[:] #generates a string comprising of all characters a to z
    available=list(a) # coverting that above string to a list
    for i in lettersGuessed:
        available.remove(i)  #removing the guessed characters

    return ''.join(available)  #returning the list as string


def hangman(secretWord):
    '''
    Starts up an interactive game of Hangman.
    '''
    len_secret_word=len(secretWord) #gives the length of secret word
    guesses_left=8
    print "Welcome to the game, Hangman!"
    print "I am thinking of a word that is %d letters long"%len_secret_word
    print "-------------"
    letters_guessed=[] #list for keeping track of letters guessed

    while guesses_left >=1: #if sufficient guesses are remaining
        print "You have %d guesses left"%guesses_left
        print "Available letters:",getAvailableLetters(letters_guessed) #shows the letters available for users
        print "Please guess a letter:",
        guess_letter=raw_input() #stores the guess letter of the user
        guess_letter=guess_letter.lower()
        if(guess_letter in letters_guessed): #checking whether user has already entered that letter
            print "Oops! You've already guessed that letter:",getGuessedWord(secretWord,letters_guessed)
        elif(guess_letter not in secretWord): #check whether letter is not present in secret word
            print "Oops! That letter is not in my word:",getGuessedWord(secretWord,letters_guessed)
            letters_guessed.append(guess_letter) #appending a list that will be used for keeping track of user's choices
            guesses_left-=1 #a wasted guess
        else:
            letters_guessed.append(guess_letter)
            print "Good guess:",getGuessedWord(secretWord,letters_guessed)
        print "-------------"

        if (isWordGuessed(secretWord,letters_guessed)):
            print "Congratulations, you won!"
            break

    else:
         print "Sorry, you ran out of guesses. The word was %s."%secretWord


secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
