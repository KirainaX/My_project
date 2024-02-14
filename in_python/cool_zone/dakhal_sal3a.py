from ta7wil import talaja_cont, sabon_cont  # Importing functions for displaying content

def dakhal_sal3a():
    talajaList = []  # List to store inputs related to refrigerators
    sabonList = []   # List to store inputs related to washing machines
    
    # Instructions for the user
    print("==> Fin ba4i dakhal sal3a?")
    print("     • Ila 4adi dakhal sal3a dyal talajat dakhal ra9am '1'")
    print("     • Ila 4adi dakhal sal3a dyal makinat sabon dakhal ra9am '2'")
    
    while True:  # Infinite loop to keep prompting user until valid input
        talajaDict = {}  # Dictionary to store refrigerator items and prices
        sabonDict = {}   # Dictionary to store washing machine items and prices
        
        # Reading refrigerator items and prices from file
        myFile = open("refrigerator_quantity.txt")
        L = myFile.readlines()
        myFile.close()
        fileList = [s[:-1] if s.endswith('\n') else s for s in L]
        for item in fileList:
            itemName = item.split()[0]
            itemPrice = item.split()[1]
            talajaDict.update({itemName: int(itemPrice)})
        
        # Reading washing machine items and prices from file
        myFile = open("washing_machine_quantity.txt")
        L = myFile.readlines()
        myFile.close()
        fileList = [s[:-1] if s.endswith('\n') else s for s in L]
        for item in fileList:
            itemName = item.split()[0]
            itemPrice = item.split()[1]
            sabonDict.update({itemName: int(itemPrice)})
        
        # Prompting user for input
        sal3a = input("==> dakhal ra9am liba4i: ")
        
        if sal3a.isdigit(): # Checking if input is a digit
            sal3a = int(sal3a)
            if sal3a == 1:  # If user chooses refrigerators
                while True:
                    p = input("• dakhal smiya dyal sal3a: ")# Prompting for refrigerator name
                    p = p.replace(' ', '-')
                    while p not in talajaDict.keys():  # Validating if entered name exists in dictionary
                        print("==> had smiya li dakhalty mkynach fstok!")
                        p = input("• 3awd dakhal smiya dyal sal3a: ")
                        if p in talajaDict:  # If name exists, continue to next step
                            continue
                    c = input("• dakhal kamiya dyal had sal3a: ")  # Prompting for quantity
                    talajaList.append(p.replace(' ', '-') + ' ' + c)  # Appending input to the list
                    jawab = input("==> ba9i ba4i dakhal sal3a?\ndakhal 'a' ila knty adakhal sal3a akhra\ndakhal 'l' ila knty sf atkhroj: ")
                    while jawab.lower() not in ['a', 'l']:  # Validating user's response
                        print("• madakhaltich ikhtiyar s7i7 :(")
                        jawab = input("==> ba9i ba4i dakhal sal3a?\ndakhal 'a' ila knty adakhal sal3a akhra\ndakhal 'l' ila knty sf atkhroj: ")
                    if jawab.lower() == 'l':  # If user wants to exit, break the loop
                        break
            elif sal3a == 2:  # If user chooses washing machines
                while True:
                    p = input("==> dakhal smiya dyal sal3a: ")  # Prompting for washing machine name
                    p = p.replace(' ', '-')
                    while p not in sabonDict.keys():  # Validating if entered name exists in dictionary
                        print("• had smiya li dakhalty mkynach fstok!")
                        p = input("==> 3awd dakhal smiya dyal sal3a: ")
                        if p in sabonDict:  # If name exists, continue to next step
                            continue
                    c = input("• dakhal kamiya dyal had sal3a: ")  # Prompting for quantity
                    sabonList.append(p.replace(' ', '-') + ' ' + c)  # Appending input to the list
                    jawab = input("==> ba9i ba4i dakhal sal3a?\ndakhal 'a' ila knty adakhal sal3a akhra\ndakhal 'l' ila knty sf atkhroj: ")
                    while jawab.lower() not in ['a', 'l']:  # Validating user's response
                        print("==> madakhaltich ikhtiyar s7i7 :(")
                        jawab = input("==> ba9i ba4i dakhal sal3a?\ndakhal 'a' ila knty adakhal sal3a akhra\ndakhal 'l' ila knty sf atkhroj: ")
                    if jawab.lower() == 'l':  # If user wants to exit, break the loop
                        break
        else:
            print("==> dakhalty ra9am mkynch bin [1, 2] dakhal wa7ad fihom")  # Error message for invalid input
            continue
        break  # Exit the loop when done with user inputs
    
    if sal3a == 1:  # If user chose refrigerators
        talaja_cont(talajaList)  # Calling function to display refrigerator contents
    else:
        sabon_cont(sabonList)  # Calling function to display washing machine contents
