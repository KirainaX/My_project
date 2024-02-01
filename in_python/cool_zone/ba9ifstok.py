from tzidfstok import talaja_cnt, sabon_cnt

def ba9i_fstok():
    kolchy_cnt = {**talaja_cnt, **sabon_cnt}
    kolchy_cnt = dict(sorted(kolchy_cnt.items()))
    count = 0
    for k, v in kolchy_cnt.items():
        if v > 1:
            print(f"{k}: {v}", end="")
            print(" 7abat")
        elif v == 0:
            print(f"{k}: ", end="")
            print("mab9ach")
        else:
            print(f"{k}: {v}", end="")
            print(" 7aba")
        count+=1
