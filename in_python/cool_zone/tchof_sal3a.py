def tchof_sal3a():
    # Printing instructions for the user to choose between options
    print("==> chmn sal3a ba4i tchof ?")
    print("• ila knty ba4i tchof stok dyal talajat dakhal '1'.")
    print("• ila knty ba4i tchof stok dyal makinat sabon dakhal '2'.")
    
    # Asking user for input
    ikhtiyar = int(input("ikhtiyark: "))
    
    # Loop to validate user input until it meets the requirements
    while True:
        if type(ikhtiyar) is not int:
            # If input is not an integer, prompting the user to input again
            print("==> ma dakhaltich ra9am")
            print("• ila knty ba4i tchof stok dyal talajat dakhal '1'.")
            print("• ila knty ba4i tchof stok dyal makinat sabon dakhal '2'.")
            ikhtiyar = int(input("ikhtiyark: "))
        elif ikhtiyar not in [1, 2]:
            # If input is not 1 or 2, prompting the user to input again
            print("==> dakhalty ra9am mkynch bin [1, 2] dakhal wa7ad fihom")
            print("• ila knty ba4i tchof stok dyal talajat dakhal '1'.")
            print("• ila knty ba4i tchof stok dyal makinat sabon dakhal '2'.")
            ikhtiyar = int(input("ikhtiyark: "))
        else:
            # If input is valid, proceed to execute respective option
            if ikhtiyar == 1:
                # Handling option 1: Displaying remaining stock of talajat
                talajaDict = {}
                myFile = open("refrigerator_quantity.txt")
                L = myFile.readlines()
                myFile.close()
                fileList = [s[:-1] if s.endswith('\n') else s for s in L]
                print("------ sal3a li ba9a fstok dyal taljat ------         ")
                for item in fileList:
                    itemName = item.split()[0]
                    itemcont = item.split()[1]
                    talajaDict.update({itemName: int(itemcont)})
                    for itemName in talajaDict.keys():
                        itemName = itemName.replace('-', ' ')
                    if int(itemcont) > 2:
                        print(f"        {itemName} : {itemcont} 7abat")
                    elif int(itemcont) == 1:
                        print(f"        {itemName} : kyna 4ir 7aba wa7da")
                    elif int(itemcont) == 2:
                        print(f"        {itemName} : kyna 4ir joj 7abat")
            elif ikhtiyar == 2:
                # Handling option 2: Displaying remaining stock of washing machine soap
                sabonDict = {}
                myFile = open("washing_machine_quantity.txt")
                L = myFile.readlines()
                myFile.close()
                fileList = [s[:-1] if s.endswith('\n') else s for s in L]
                print("------ sal3a li ba9a fstok dyal makinat sabon ------         ")
                for item in fileList:
                    itemName = item.split()[0]
                    itemcont = item.split()[1]
                    sabonDict.update({itemName: int(itemcont)})
                    for itemName in sabonDict.keys():
                        itemName = itemName.replace('-', ' ')
                    if int(itemcont) > 2:
                        print(f"        {itemName} : {itemcont} 7abat")
                    elif int(itemcont) == 1:
                        print(f"        {itemName} : kyna 4ir 7aba wa7da")
                    elif int(itemcont) == 2:
                        print(f"        {itemName} : kyna 4ir joj 7abat")
        break  # Exiting the loop after executing the chosen option
