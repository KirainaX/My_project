def talaja_cont(talajaList):
    talajaDict = {}
    myFile = open("refrigerator_quantity.txt")

    L = myFile.readlines()
    print(L)
    myFile.close()

    fileList = [s[:-1] if s.endswith('\n') else s for s in L]
    print(fileList)

    print("talaja List: {}".format(talajaList))
    print("\n\n\n")
    for itme in fileList:
        itmeName = itme.split()[0]
        itmePrice = itme.split()[1]
        talajaDict.update({itmeName: itmePrice})
    for k, v in talajaDict.items():
        print(f"{k}: {v}")

    talajaDict["Capilre"] = 2345

    with open("y.txt", 'w') as f:
        for k, v in talajaDict.items():
            product = k + ' ' + str(v) + '\n'
            f.write(product)