'''from talajacntstok import talaja_cnt
from saboncntstok import sabon_cnt'''
import pickle
import os

def tzid_fstok():
    fileName = "/home/ubuntu/ubuntu/My_project/in_python/cool_zone/talajacntstok.pkl"

    print("ba4i tzid f talajat dakhal '1'")
    print("ba4i tzid f makinat sabon dakhal '2'")
    stor = int(input("ikhtiyark "))
    
    if stor == 1:
        if os.path.exists(fileName):
            with open(fileName, 'rb') as f:
                employee = pickle.load(f)
        else:
            employee = {}

        while True:
            key = input("dakhal smiyat sal3a (type 'exit' to finish): ")
            if key.lower() == 'exit':
                break
                
            value = input("dakhal contity li jat: ")
            employee[key] = value

        with open(fileName, 'wb') as f:
            pickle.dump(employee, f)

        print(employee)

    # Uncomment the following block if you want to handle option 2
    # elif stor == 2:
    #     key = input("dakhal smiyat sal3a: ")
    #     if key not in sabon_cnt:
    #         print("had smiya lidakhalty mkynach fi stok")
    #         print("3awad dakhal smiya")
    #         key = input("dakhal smiyat sal3a: ")
    #     value = input("dakhal contity li jat: ")
    #     if key in sabon_cnt:
    #         sabon_cnt.update({key: value})

# Call the function








        '''elif stor == 2:
            key = input("dakhal smiyat sal3a: ")
            if key not in sabon_cnt:
                print("had smiya lidakhalty mkynach fi stok")
                print("3awad dakhal smiya")
                key = input("dakhal smiyat sal3a: ")
            value = input("dakhal contity li jat: ")
            if key in sabon_cnt:
                sabon_cnt.update({key: value})
            break'''

tzid_fstok()