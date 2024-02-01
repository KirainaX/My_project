from ba9ifstok import ba9i_fstok
from tzidfstok import tzid_fstok
from kliyann import kliyan

print("============================")
print("ila b4ity chno ba9i fstok dakhal '1'")
print("ila b4ity tzid sal3a fstok dakhal '2'")
print("ila b4ity t5araj kliyan sal3a dakhal '3'")
khtiyar = int(input("ikhtiyark "))

while True:
    if khtiyar == 1:
        ba9i_fstok()
        break
    elif khtiyar == 2:
        tzid_fstok()
        break
    elif khtiyar == 3:
        print("ba4i tzid f talajat dakhal '1'")
        print("ba4i tzid f makinat sabon dakhal '2'")
        stor = int(input("ikhtiyark "))
        kliyan(stor)
        break
    else:
        print("khtarity ra9am mkynch idan 3awad khtar hhh")
        print("ila b4ity chno ba9i fstok dakhal '1'")
        print("ila b4ity tzid sal3a fstok dakhal '2'")
        print("ila b4ity t5araj kliyan sal3a dakhal '3'")
        khtiyar = int(input("ikhtiyark "))