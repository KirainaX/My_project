def dakhal_sal3a():
    talajaDict = {}
    talajaFileList = []
    talajaList = []
    #read data from text file
    talajat = open("refrigerator_quantity.txt")
    T = talajat.readlines()
    talajat.close()
    talajaFileList = [s[:-1] if s.endswith('\n') else s for s in T]
    #print(talajaFileList)
    print("Fin ba4i dakhal sal3a?")
    print("     • Ila 4adi dakhal sal3a dyal talajat dakhal ra9am '1'")
    print("     • Ila 4adi dakhal sal3a dyal makinat sabon dakhal ra9am '2'")
    sal3a = int(input("dakhal ra9am liba4i: "))
    while True:
        if (sal3a > 2) or (sal3a < 1):
            print("dakhalty ra9am mkynch bin [1, 2] dakhal wa7ad fihom")
            print("     • Ila 4adi dakhal sal3a dyal talajat dakhal ra9am '1'")
            print("     • Ila 4adi dakhal sal3a dyal makinat sabon dakhal ra9am '2'")
            sal3a = int(input("dakhal ra9am liba4i: "))
        else:
            if sal3a == 1:
                p = input("dakhal smiya dyal sal3a : ")
                c = input("dakhal kamiya dyal had sal3a: ")
                talajaList.append(p.replace(' ', '-'))
                talajaList.append(c)
                jawab = input("ba9i ba4i dakhal sal3a? dakhal 'a' ila knty adakhal mazal awla dakhal 'n' ila knty sf atkhroj: ")
                if jawab.lower() == 'a':
                    p = input("dakhal smiya dyal sal3a : ")
                    c = input("dakhal kamiya dyal had sal3a: ")
                    talajaList.append(p.replace(' ', '-'))
                    talajaList.append(c)
                    jawab = input("ba9i ba4i dakhal sal3a? dakhal 'a' ila knty adakhal mazal awla dakhal 'n' ila knty sf atkhroj: ")
                elif jawab.lower() == 'n':
                    break
                else:
                    while True:
                        print("rak madakhaltich jawab s7i7 :(")
                        jawab = input("ba9i ba4i dakhal sal3a? dakhal 'a' ila knty adakhal mazal awla dakhal 'n' ila knty sf atkhroj: ")
                        break
                print(talajaList)
                talajaDict["Capilre"] = 2345

                with open("y.txt", 'w') as f:
                    for k, v in talajaDict.items():
                        vuu = k + ' ' + str(v) + '\n'
                        f.write(vuu)
                break
            #elif sal3a == 2:
