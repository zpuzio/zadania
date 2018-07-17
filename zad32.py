def random_word():
    import random
    a = []
    with open('slownik.txt', 'r') as f:
      line = f.readline()
      while line:
        a.append(line)
        line = f.readline()
    word = random.randint(0,len(a))
    return a[word]

def game(word,chance,line,usedLetters):
    letters = []
    user = raw_input("Podaj litere: ").upper()
    for letter in word.upper():
        letters.append(letter)
    if chance == 1:
        print "Przegrales"
        again = raw_input("Chcesz grac dalej [t/n]: ")
        if again == "t":
            return main()
        else:
            exit()
    if user in usedLetters:
        print "Juz wpisywales ta litere"
        return game(word, chance, line, usedLetters)
    if user in letters:
        usedLetters.append(user)
        checkDuplicate = [char for char, u in enumerate(letters) if u == user]
        if len(checkDuplicate) == 1:
            line[checkDuplicate[0]] = user
            print " ".join(line)
            if "__" not in line:
                print "Wygrales!"
                exit()
            return game(word, chance, line,usedLetters)
        elif len(checkDuplicate) != 0:
            for item in checkDuplicate:
                line[item] = user
            print " ".join(line)
            if "__" not in line:
                print "Wygrales!"
                again = raw_input("Chcesz grac dalej [t/n]: ")
                if again == "t":
                    return main()
                else:
                    exit()
            return game(word, chance, line, usedLetters)
    else:
        usedLetters.append(user)
        chance -= 1
        print "Nie ma takiej litery, zostalo Ci " + str(chance) +" szans"
        return game(word,chance,line,usedLetters)
    return (chance, line)

def main():
    word = random_word()
    print word
    lines = []
    usedLetters = []
    for line in range(len(word) - 1):
        lines.append("__")

    print "Grasz w wisielca!"
    print "Masz 6 szans"
    print " ".join(lines)
    c = 6
    result = game(word, c, lines, usedLetters)

if __name__=="__main__":
    main()


