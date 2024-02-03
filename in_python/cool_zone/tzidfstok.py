from talajacntstok import talaja_cnt
from saboncntstok import sabon_cnt

def tzid_fstok():

    print("ba4i tzid f talajat dakhal '1'")
    print("ba4i tzid f makinat sabon dakhal '2'")
    stor = int(input("ikhtiyark "))
    while True:
        if stor == 1:
            key = input("dakhal smiyat sal3a: ")
            if key not in talaja_cnt:
                print("had smiya lidakhalty mkynach fi stok")
                print("3awad dakhal smiya")
                key = input("dakhal smiyat sal3a: ")    
            value = input("dakhal contity li jat: ")
            if key in talaja_cnt:
                talaja_cnt.update({key: value})
                print(talaja_cnt)
            break
        elif stor == 2:
            key = input("dakhal smiyat sal3a: ")
            if key not in sabon_cnt:
                print("had smiya lidakhalty mkynach fi stok")
                print("3awad dakhal smiya")
                key = input("dakhal smiyat sal3a: ")
            value = input("dakhal contity li jat: ")
            if key in sabon_cnt:
                sabon_cnt.update({key: value})
            break

tzid_fstok()