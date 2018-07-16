def horizontal(size):
    print(" --- " * size)

def vertical(size):
    print("|    " * (size +1))

if __name__=="__main__":
    size = int(raw_input("Podaj rozmiar tablicy np. 3: "))
    for i in range(0, size):
        horizontal(size)
        vertical(size)
    horizontal(size)