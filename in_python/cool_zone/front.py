from dakhal_sal3a import dakhal_sal3a
from tchof_sal3a import tchof_sal3a

print("         ------ Mar7ba bikom fi Cool Zone ------         ")
print("• Ila b4ity dakhal sal3a lstok dakhal ra9am '1'")
print("• Ila b4ity tchof sal3a liba9a lik fstok dakhal ra9am '2'")
print("• Ila knty ba4i tjma3 sal3a lkliyan dakhal ra9am '3'")
userInput = int(input("Dakhal ra9am liba4i: "))

while True:
    if type(userInput) is not int:
        print("==> ma dakhaltich ra9am")
        print("     • Ila b4ity dakhal sal3a lstok dakhal ra9am '1'")
        print("     • Ila b4ity tchof sal3a liba9a lik fstok dakhal ra9am '2'")
        print("     • Ila knty ba4i tjma3 sal3a lkliyan dakhal ra9am '3'")
        userInput = int(input("     Dakhal ra9am liba4i: "))
    elif userInput not in [1, 2, 3]:
        print("==> dakhalty ra9am mkynch bin [1, 2, 3] dakhal wa7ad fihom")
        print("     • Ila b4ity dakhal sal3a lstok dakhal ra9am '1'")
        print("     • Ila b4ity tchof sal3a liba9a lik fstok dakhal ra9am '2'")
        print("     • Ila knty ba4i tjma3 sal3a lkliyan dakhal ra9am '3'")
        userInput = int(input("     Dakhal ra9am liba4i: "))
    else:
        if userInput == 1:
            dakhal_sal3a()
            break
        elif userInput == 2:
            tchof_sal3a()
            break
        #elif userInput == 3: