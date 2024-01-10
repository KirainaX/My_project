import random
from hgmtools import words, print_hangman

def get_word():
    word = random.choice(words)
    return word.upper()
def play(word):
    wordCompletion = '_' * len(word)
    guessed = False
    guessedLetters = []
    guessedWords = []
    tries = 0
    print("Lest's play Hangman!")
    print_hangman(tries)
    print(wordCompletion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessedLetters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word")
                tries += 1
                guessedLetters.append(guess)
            else:
                print("Good job,", guess, "is in the word!")
                guessedLetters.append(guess)
                wordAsList = list(wordCompletion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    wordAsList[index]
        elif len(guess) == len(word) and guess.isalpha:

        else:
            print("Not a valid guess.")
        print(print_hangman(tries))
        print(wordCompletion)
        print("\n")
