#read data from text file
productDict = {}
fileList = []
list = []
myFile = open("refrigerator_quantity.txt")

L = myFile.readlines()
#print(L)
myFile.close()

fileList = [s[:-1] if s.endswith('\n') else s for s in L]
print(fileList)

print(fileList)
for itme in fileList:
    itmeName = itme.split()[0]
    itmePrice = itme.split()[1]
    productDict.update({itmeName: itmePrice})
for k, v in productDict.items():
    print(f"{k}: {v}")

productDict["Capilre"] = 123

with open("refrigerator_quantity.txt", 'w') as f:
    for k, v in productDict.items():
        product = k + ' ' + str(v) + '\n'
        f.write(product)
