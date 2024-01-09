import random

anime_list = ["Naruto", "Dragon Ball", "One Piece", "Shingeki no Kyojin", "Death Note", "Fullmetal Alchemist", "Boku no Hero Academia", "Sword Art Online", "Tokyo Ghoul", 
"Kimetsu no Yaiba", "Cowboy Bebop", "Hunter x Hunter", "Spirited Away", "One Punch Man", "Bleach", "Fairy Tail", "Pokemon", "Your Lie in April", "Death Parade", "Code Geass", 
"JoJo", "Haikyuu", "Yakusoku no Neverland", "Steins Gate", "Black Clover", "Naruto Shippuden", "Mob Psycho 100", "Inuyasha", "Beastars", "Jujutsu Kaisen", "Trigun", 
"Assassination Classroom", "Durarara", "Parasyte", "Toradora", "Great Teacher Onizuka", "Erased", "Akira", "Dorohedoro", "Hellsing", "Tokyo Revengers", 
"Made in Abyss", "A Silent Voice", "Blue Exorcist", "Charlotte", "Soul Eater", "Nanatsu no Taizai", "Re Zero", "Pandora Hearts", "Psycho-Pass", "Noragami", "Black Butle", 
"Dororo", "Chainsaw Man", "Blue Lock", "Shaman King", "Dr Stone", "Detective Conan", "Fire Force", "Viland Saha"]

random_anime = random.choice(anime_list)
print(random_anime)
len_random = len(random_anime)
midl = len_random // 2
print(midl)
print(len_random)

for chr in random_anime:
    if chr == ' ':
        idx = random_anime.index(chr)
        #print(idx, end="")

        print(' ', end='')
        print(f'{chr} ({idx})', end='')
        #random_anime = random_anime.replace(random_anime[idx], '*')
    elif (chr == random_anime[0]) or (chr == random_anime[midl]) or (chr == random_anime[len_random -2]):
        print(chr, end='')    
    else:
        print('-', end='')
print("")
