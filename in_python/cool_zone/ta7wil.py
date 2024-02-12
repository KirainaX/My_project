# Define a function to update quantities of items in a refrigerator
def talaja_cont(talajaList):
    # Initialize dictionaries to store current and new quantities of items
    talajaDict = {}
    newtalajaDict = {}
    
    # Open the file containing current quantities of items in the refrigerator
    myFile = open("refrigerator_quantity.txt")
    L = myFile.readlines()  # Read lines from the file
    myFile.close()  # Close the file
    
    # Remove newline characters from the end of each line and store in a list
    fileList = [s[:-1] if s.endswith('\n') else s for s in L]
    
    # Populate the current quantities dictionary with items and their quantities
    for item in fileList:
        itemName = item.split()[0]  # Extract item name
        itemPrice = item.split()[1]  # Extract item price
        talajaDict.update({itemName: int(itemPrice)})  # Update dictionary
    
    # Populate the new quantities dictionary with items and their quantities
    for item in talajaList:
        itemName = item.split()[0]  # Extract item name
        itemPrice = item.split()[1]  # Extract item price
        newtalajaDict.update({itemName: int(itemPrice)})  # Update dictionary
    
    # Update the quantities of items in the current quantities dictionary
    for itemName in talajaDict:
        if itemName in newtalajaDict:
            talajaDict[itemName] = talajaDict[itemName] + newtalajaDict[itemName]
    
    # Write the updated quantities to the file
    with open("refrigerator_quantity.txt", 'w') as f:
        for itemName, itemQuantity in talajaDict.items():
            product = itemName + ' ' + str(itemQuantity) + '\n'
            f.write(product)
    
    # Print confirmation message
    print("Done!")

# Define a function to update quantities of items in a washing machine
def sabon_cont(sabonList):
    # Initialize dictionaries to store current and new quantities of items
    sabonDict = {}
    newsabonDict = {}
    
    # Open the file containing current quantities of items in the washing machine
    myFile = open("washing_machine_quantity.txt")
    L = myFile.readlines()  # Read lines from the file
    myFile.close()  # Close the file
    
    # Remove newline characters from the end of each line and store in a list
    fileList = [s[:-1] if s.endswith('\n') else s for s in L]
    
    # Populate the current quantities dictionary with items and their quantities
    for item in fileList:
        itemName = item.split()[0]  # Extract item name
        itemPrice = item.split()[1]  # Extract item price
        sabonDict.update({itemName: int(itemPrice)})  # Update dictionary
    
    # Populate the new quantities dictionary with items and their quantities
    for item in sabonList:
        itemName = item.split()[0]  # Extract item name
        itemPrice = item.split()[1]  # Extract item price
        newsabonDict.update({itemName: int(itemPrice)})  # Update dictionary
    
    # Update the quantities of items in the current quantities dictionary
    for itemName in sabonDict:
        if itemName in newsabonDict:
            sabonDict[itemName] = sabonDict[itemName] + newsabonDict[itemName]
    
    # Write the updated quantities to the file
    with open("washing_machine_quantity.txt", 'w') as f:
        for itemName, itemQuantity in sabonDict.items():
            product = itemName + ' ' + str(itemQuantity) + '\n'
            f.write(product)
    
    # Print confirmation message
    print("Done!")
