productDict = {}
fileList = []
list = []
#read data from text file
myFile = open("refrigerator_quantity.txt")

L = myFile.readlines()
#print(L)
myFile.close()

fileList = [s[:-1] if s.endswith('\n') else s for s in L]
print(fileList)

for itme in fileList:
    itmeName = itme.split()[0]
    itmePrice = itme.split()[1]
    productDict.update({itmeName: itmePrice})
for k, v in productDict.items():
    print(f"{k}: {v}")

productDict["Capilre"] = 2345

with open("refrigerator_quantity.txt", 'w') as f:
    for k, v in productDict.items():
        product = k + ' ' + str(v) + '\n'
        f.write(product)


'''for i in talajaFileList:
    iName = i.split()[0]
    iPrice = i.split()[1]
    talajaDict.update({iName: iPrice})
for k, v in talajaDict.items():
    print(f"{k}: {v}")'''