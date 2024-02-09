# Define a function to update the quantity of items in the refrigerator based on a list of items
def talaja_cont(talajaList):
    # Create an empty dictionary to store items and their quantities from the refrigerator file
    talajaDict = {}
    # Create a new dictionary to store updated quantities
    newtalajaDict = {}
    # Open the file containing the refrigerator quantities
    myFile = open("refrigerator_quantity.txt")
    # Read all lines from the file and store them in a list
    L = myFile.readlines()
    myFile.close()  # Close the file

    # Remove newline characters from each line and store in fileList
    fileList = [s[:-1] if s.endswith('\n') else s for s in L]
    
    # Parse each line in fileList to extract item names and prices, and store them in talajaDict
    for item in fileList:
        itemName = item.split()[0]
        itemPrice = item.split()[1]
        talajaDict.update({itemName: itemPrice})
    
    # Parse each item in talajaList to extract names and prices, and store them in newtalajaDict
    for item in talajaList:
        itemName = item.split()[0]
        itemPrice = item.split()[1]
        newtalajaDict.update({itemName: itemPrice})

    # Update the quantities in talajaDict based on newtalajaDict
    for itemName, itemPrice in newtalajaDict.items():
        for oldItemPrice in talajaDict.values():
            if itemName in talajaDict.keys():
                talajaDict[itemName] = int(itemPrice) + int(oldItemPrice)

    # Write the updated quantities to the refrigerator file
    with open("refrigerator_quantity.txt", 'w') as f:
        for itemName, itemQuantity in talajaDict.items():
            product = itemName + ' ' + str(itemQuantity) + '\n'
            f.write(product)  # Write the item name and quantity to the file
    print("Done!")

# Define a function to update the quantity of items in the washing machine based on a list of items
def sabon_cont(sabonList):
    # Create an empty dictionary to store items and their quantities from the washing machine file
    sabonDict = {}
    # Create a new dictionary to store updated quantities
    newsabonDict = {}
    # Open the file containing the washing machine quantities
    myFile = open("washing_machine_quantity.txt")
    # Read all lines from the file and store them in a list
    L = myFile.readlines()
    myFile.close()  # Close the file

    # Remove newline characters from each line and store in fileList
    fileList = [s[:-1] if s.endswith('\n') else s for s in L]
    
    # Parse each line in fileList to extract item names and prices, and store them in sabonDict
    for item in fileList:
        itemName = item.split()[0]
        itemPrice = item.split()[1]
        sabonDict.update({itemName: itemPrice})
    
    # Parse each item in sabonList to extract names and prices, and store them in newsabonDict
    for item in sabonList:
        itemName = item.split()[0]
        itemPrice = item.split()[1]
        newsabonDict.update({itemName: itemPrice})

    # Update the quantities in sabonDict based on newsabonDict
    for itemName, itemPrice in newsabonDict.items():
        for oldItemPrice in sabonDict.values():
            if itemName in sabonDict.keys():
                sabonDict[itemName] = int(itemPrice) + int(oldItemPrice)

    # Write the updated quantities to the washing machine file
    with open("washing_machine_quantity.txt", 'w') as f:
        for itemName, itemQuantity in sabonDict.items():
            product = itemName + ' ' + str(itemQuantity) + '\n'
            f.write(product)  # Write the item name and quantity to the file
    print("Done!")
