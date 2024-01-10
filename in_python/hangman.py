import random

from hgmtools import animeList, print_hangman

wrongGuess = 0
print("Let's play Hangman!")

def get_anime():
    randomAnime = random.choice(animeList)
    return randomAnime.upper()

def has_multiple_words(input_string):
    words = input_string.split()
    return len(words) > 1

def print_anime_name(name):
    for x in name:
        if x == '*':
            print(' ', end="")
        elif x != '*':
            print('_', end=' ')
    print('')

'''def player_input():
    playerGuess = input("")'''

animeName = get_anime()
print(animeName)
check = has_multiple_words(animeName)
if check == True:
    nameStar = animeName.split()
    nameStar = '*'.join(nameStar)
    print_anime_name(nameStar)
else:
    print_anime_name(animeName)
    





'''for i in range(7):
    print_hangman(i)
    print(i)'''

