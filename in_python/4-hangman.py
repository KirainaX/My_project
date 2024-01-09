import random
from hgmtools import anime_list

def has_multiple_words(input_string):
    words = input_string.split()
    return len(words) > 1


def print_random_anime(anime):
    if type(anime) != list:
        dach = []
        c1 = len(anime) - 1
        ch = c1 // 2
        nw_anime = anime[1:ch] + anime[ch + 1:c1 - 1]
        for i in nw_anime:
            dach.append('-')
        dach = ''.join(dach)
        c2 = len(dach)
        all_name = anime[0] + dach[:c2 // 2 + 1] + anime[ch] + dach[(c2 // 2):] + anime[c1]
        return all_name
    else:
        dach = []
        for i in anime:
            for j in i:
                l1 = len(i) - 1
                l1h = l1 // 2
                if l1 == 1 or l1 == 2:
                    if l1 == 1:
                        dach.append(i)
                    else:
                        dach.append(i[0]+'-')
                elif l1 == 3:
                    dach.append(i[0]+'-'+i[l1])
                else:
                    dach2 = []
                    nw_anime = i[1:l1h] + i[l1h + 1:l1 - 1]
                    for i in nw_anime:
                        dach2.append('-')
                    dach = ''.join(dach2)
                    l2 = len(dach)
                    print(dach)
                    #dach = i[0] + dach[:(l2 // 2) + 1] + i[l1h] + dach[(l2 // 2):] + i[l1]

        
                

random_anime = random.choice(anime_list)

print(random_anime)

new_random = has_multiple_words(random_anime)
if new_random == True:
    new_random = random_anime.split()
    t = print_random_anime(new_random)
    print(t)

else:
    t = print_random_anime(random_anime)
    print(t)

print(new_random)
