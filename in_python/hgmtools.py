words = ["Dororo", "Erased", "Akira", "Dorohedoro", "Hellsing", "Pokemon"]
animeList = ["Yakusoku no Neverland"]
#animeList = ["Neverland"]
'''["Naruto", "Dragon Ball", "One Piece", "Shingeki no Kyojin", "Death Note", "Fullmetal Alchemist", "Boku no Hero Academia", "Sword Art Online", "Tokyo Ghoul", 
"Kimetsu no Yaiba", "Cowboy Bebop", "Hunter x Hunter", "Spirited Away", "One Punch Man", "Bleach", "Fairy Tail", "Pokemon", "Your Lie in April", "Death Parade", "Code Geass", 
"JoJo", "Haikyuu", "Yakusoku no Neverland", "Steins Gate", "Black Clover", "Naruto Shippuden", "Mob Psycho 100", "Inuyasha", "Beastars", "Jujutsu Kaisen", "Trigun", 
"Assassination Classroom", "Durarara", "Parasyte", "Toradora", "Great Teacher Onizuka", "Erased", "Akira", "Dorohedoro", "Hellsing", "Tokyo Revengers", 
"Made in Abyss", "A Silent Voice", "Blue Exorcist", "Charlotte", "Soul Eater", "Nanatsu no Taizai", "Re Zero", "Pandora Hearts", "Psycho-Pass", "Noragami", "Black Butle", 
"Dororo", "Chainsaw Man", "Blue Lock", "Shaman King", "Dr Stone", "Detective Conan", "Fire Force", "Viland Saha"]'''

def print_hangman(tries):
    
    if (tries == 0):
        print("    ------")
        print("    |    |")
        print("    |     ")
        print("    |     ")
        print("    |     ")
        print("    |     ")
        print("    |     ")
        print("------------")
    elif (tries == 1):
        print("    ------")
        print("    |    |")
        print("    |    O")
        print("    |     ")
        print("    |     ")
        print("    |     ")
        print("    |     ")
        print("------------")
    elif (tries == 2):
        print("    ------")
        print("    |    |")
        print("    |    O")
        print("    |    |")
        print("    |     ")
        print("    |     ")
        print("    |     ")
        print("------------")
    elif (tries == 3):
        print("    ------")
        print("    |    |")
        print("    |    O")
        print("    |   /|")
        print("    |     ")
        print("    |     ")
        print("    |     ")
        print("------------")
    elif (tries == 4):
        print("    ------")
        print("    |    |")
        print("    |    O")
        print("    |   /|\\")
        print("    |     ")
        print("    |     ")
        print("    |     ")
        print("------------")
    elif (tries == 5):
        print("    ------")
        print("    |    |")
        print("    |    O")
        print("    |   /|\\")
        print("    |   /")
        print("    |     ")
        print("    |     ")
        print("------------")
    elif (tries == 6):
        print("    ------")
        print("    |    |")
        print("    |    O")
        print("    |   /|\\")
        print("    |   / \\")
        print("    |     ")
        print("    |     ")
        print("------------")
