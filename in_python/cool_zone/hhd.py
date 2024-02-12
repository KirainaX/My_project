talajaDict = {}
myFile = open("refrigerator_quantity.txt")
L = myFile.readlines()
myFile.close()
fileList = [s[:-1] if s.endswith('\n') else s for s in L]
for item in fileList:
    itemName = item.split()[0]
    itemPrice = item.split()[1]
    talajaDict.update({itemName: int(itemPrice)})


sabonDict = {}
myFile = open("washing_machine_quantity.txt")
L = myFile.readlines()
myFile.close()
fileList = [s[:-1] if s.endswith('\n') else s for s in L]
for item in fileList:
    itemName = item.split()[0]
    itemPrice = item.split()[1]
    sabonDict.update({itemName: int(itemPrice)})