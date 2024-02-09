from ta7wil import talaja_cont

def dakhal_sal3a():
    talajaList = []
    
    print("Fin ba4i dakhal sal3a?")
    print("     • Ila 4adi dakhal sal3a dyal talajat dakhal ra9am '1'")
    print("     • Ila 4adi dakhal sal3a dyal makinat sabon dakhal ra9am '2'")
    sal3a = int(input("==> dakhal ra9am liba4i: "))
    while True:
        if not (1 <= sal3a <= 2):
            print("dakhalty ra9am mkynch bin [1, 2] dakhal wa7ad fihom")
            print("     • Ila 4adi dakhal sal3a dyal talajat dakhal ra9am '1'")
            print("     • Ila 4adi dakhal sal3a dyal makinat sabon dakhal ra9am '2'")
            sal3a = int(input("==> dakhal ra9am liba4i: "))
        else:
            if sal3a == 1:
                cut = ['a', 'l']

                p = input("dakhal smiya dyal sal3a : ")
                c = input("dakhal kamiya dyal had sal3a: ")
                talajaList.append(p.replace(' ', '-')+' '+c)
                #talajaList.append()
                jawab = input("ba9i ba4i dakhal sal3a? dakhal 'a' ila knty adakhal mazal awla dakhal 'l' ila knty sf atkhroj: ")

                while jawab.lower() not in cut:
                    print("==> madakhaltich ikhtiyar s7i7 :(")
                    jawab = input("ba9i ba4i dakhal sal3a? dakhal 'a' ila knty adakhal mazal awla dakhal 'l' ila knty sf atkhroj: ")

                if jawab.lower() == 'a':
                    continue
                else:
                    break

    talaja_cont(talajaList)
            #elif sal3a == 2:
