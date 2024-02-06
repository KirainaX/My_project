try:
    with open('test.txt') as f:
        print(f.read())
except FileNotFoundError:
    print("That file was not found :(")