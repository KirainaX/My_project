from ta7wil import talaja_cont, sabon_cont  # Importing functions from the module ta7wil

def dakhal_sal3a():
    talajaList = []  # List to store entries for "talajat"
    sabonList = []   # List to store entries for "sabon" machines

    # Displaying instructions for the user
    print("Fin ba4i dakhal sal3a?")
    print("     • Ila 4adi dakhal sal3a dyal talajat dakhal ra9am '1'")
    print("     • Ila 4adi dakhal sal3a dyal makinat sabon dakhal ra9am '2'")
    
    while True:  # Looping until valid input is received
        sal3a = input("==> dakhal ra9am liba4i: ")  # Asking user to input a number
        if sal3a.isdigit():  # Checking if input is a digit
            sal3a = int(sal3a)  # Converting input to an integer
            if sal3a == 1:  # If user selects option 1 (talajat)
                while True:  # Looping for entering details of talajat
                    p = input("dakhal smiya dyal sal3a: ")  # Asking for name of the item
                    c = input("dakhal kamiya dyal had sal3a: ")  # Asking for quantity of the item
                    talajaList.append(p.replace(' ', '-') + ' ' + c)  # Appending item name and quantity to the talajaList

                    jawab = input("ba9i ba4i dakhal sal3a? dakhal 'a' ila knty adakhal mazal awla dakhal 'l' ila knty sf atkhroj: ")  # Asking if user wants to continue entering talajat
                    while jawab.lower() not in ['a', 'l']:  # Validating user input
                        print("==> madakhaltich ikhtiyar s7i7 :(")  # Displaying error message
                        jawab = input("ba9i ba4i dakhal sal3a? dakhal 'a' ila knty adakhal mazal awla dakhal 'l' ila knty sf atkhroj: ")  # Asking again for input
                    
                    if jawab.lower() == 'l':  # If user wants to exit loop
                        break  # Breaking out of the loop
    
            elif sal3a == 2:  # If user selects option 2 (sabon)
                while True:  # Looping for entering details of sabon machines
                    p = input("dakhal smiya dyal sal3a: ")  # Asking for name of the item
                    c = input("dakhal kamiya dyal had sal3a: ")  # Asking for quantity of the item
                    sabonList.append(p.replace(' ', '-') + ' ' + c)  # Appending item name and quantity to the sabonList

                    jawab = input("ba9i ba4i dakhal sal3a? dakhal 'a' ila knty adakhal mazal awla dakhal 'l' ila knty sf atkhroj: ")  # Asking if user wants to continue entering sabon machines
                    while jawab.lower() not in ['a', 'l']:  # Validating user input
                        print("==> madakhaltich ikhtiyar s7i7 :(")  # Displaying error message
                        jawab = input("ba9i ba4i dakhal sal3a? dakhal 'a' ila knty adakhal mazal awla dakhal 'l' ila knty sf atkhroj: ")  # Asking again for input
                    
                    if jawab.lower() == 'l':  # If user wants to exit loop
                        break  # Breaking out of the loop

        else:  # If input is not a digit
            print("dakhalty ra9am mkynch bin [1, 2] dakhal wa7ad fihom")  # Displaying error message
            continue  # Restarting the loop
        
        break  # Breaking out of the loop if input is valid
    if sal3a == 1:  # If user entered talajat
        talaja_cont(talajaList)  # Calling function to handle talajat entries
    else:  # If user entered sabon machines
        sabon_cont(sabonList)  # Calling function to handle sabon machine entries
