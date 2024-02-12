def tchof_sal3a():
    # Print a prompt to select between viewing stock of talajat or makinat sabon.
    print("==> chmn sal3a ba4i tchof ?")
    print("• ila knty ba4i tchof stok dyal talajat dakhal '1'.")
    print("• ila knty ba4i tchof stok dyal makinat sabon dakhal '2'.")
    
    # Take user input for choice.
    ikhtiyar = int(input("ikhtiyark: "))
    
    # Continue looping until the user makes a valid choice.
    while True:
        # Check if the input is not an integer.
        if type(ikhtiyar) is not int:
            print("==> ma dakhaltich ra9am")
            # Prompt again for a valid choice.
            print("• ila knty ba4i tchof stok dyal talajat dakhal '1'.")
            print("• ila knty ba4i tchof stok dyal makinat sabon dakhal '2'.")
            ikhtiyar = int(input("ikhtiyark: "))
        # Check if the input is not 1 or 2.
        elif ikhtiyar not in [1, 2]:
            print("==> dakhalty ra9am mkynch bin [1, 2] dakhal wa7ad fihom")
            # Prompt again for a valid choice.
            print("• ila knty ba4i tchof stok dyal talajat dakhal '1'.")
            print("• ila knty ba4i tchof stok dyal makinat sabon dakhal '2'.")
            ikhtiyar = int(input("ikhtiyark: "))
        else:
            if ikhtiyar == 1:
                # Initialize a dictionary to store talajat stock.
                talajaDict = {}
                # Open the file containing talajat stock.
                myFile = open("refrigerator_quantity.txt")
                L = myFile.readlines()
                myFile.close()
                # Remove newline characters from each line and store in a list.
                fileList = [s[:-1] if s.endswith('\n') else s for s in L]
                print("------ sal3a li ba9a fstok dyal taljat ------         ")
                # Loop through each line in the file.
                for item in fileList:
                    # Extract item name and quantity from each line.
                    itemName = item.split()[0]
                    itemcont = item.split()[1]
                    # Update the dictionary with item name as key and quantity as value.
                    talajaDict.update({itemName: int(itemcont)})
                    # Replace '-' with ' ' in item names.
                    for itemName in talajaDict.keys():
                        itemName = itemName.replace('-', ' ')
                    # Print stock information based on quantity.
                    if int(itemcont) > 2:
                        print(f"        {itemName} : {itemcont} 7abat")
                    elif int(itemcont) == 1:
                        print(f"        {itemName} : kyna 4ir 7aba wa7da")
                    elif int(itemcont) == 2:
                        print(f"        {itemName} : kyna 4ir joj 7abat")
            elif ikhtiyar == 2:
                # Initialize a dictionary to store makinat sabon stock.
                sabonDict = {}
                # Open the file containing makinat sabon stock.
                myFile = open("washing_machine_quantity.txt")
                L = myFile.readlines()
                myFile.close()
                # Remove newline characters from each line and store in a list.
                fileList = [s[:-1] if s.endswith('\n') else s for s in L]
                print("------ sal3a li ba9a fstok dyal makinat sabon ------         ")
                # Loop through each line in the file.
                for item in fileList:
                    # Extract item name and quantity from each line.
                    itemName = item.split()[0]
                    itemcont = item.split()[1]
                    # Update the dictionary with item name as key and quantity as value.
                    sabonDict.update({itemName: int(itemcont)})
                    # Replace '-' with ' ' in item names.
                    for itemName in sabonDict.keys():
                        itemName = itemName.replace('-', ' ')
                    # Print stock information based on quantity.
                    if int(itemcont) > 2:
                        print(f"        {itemName} : {itemcont} 7abat")
                    elif int(itemcont) == 1:
                        print(f"        {itemName} : kyna 4ir 7aba wa7da")
                    elif int(itemcont) == 2:
                        print(f"        {itemName} : kyna 4ir joj 7abat")
        # Break out of the loop after processing the choice once.
        break
