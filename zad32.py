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

def win(line):
    if "__" not in line:
        print "Wygrales!"
        exit()

def game(word,chance,line,usedLetters):
    letters = []
    userInput = raw_input("Podaj litere: ").upper()
    for letter in word.upper():
        letters.append(letter)
    if chance == 1:
        print "Przegrales"
        exit()
    if userInput in usedLetters:
        print "Juz wpisywales ta litere"
        #return (chance, line, usedLetters)
        return {"chance": chance, "line": line, "usedLetters": usedLetters}
    if userInput in letters:
        usedLetters.append(userInput)
        checkDuplicate = [char for char, u in enumerate(letters) if u == userInput]
        for item in checkDuplicate:
            line[item] = userInput
        print " ".join(line)
        win(line)
        #return (chance, line, usedLetters)
        return {"chance": chance, "line": line, "usedLetters": usedLetters}
    else:
        usedLetters.append(userInput)
        chance -= 1
        print "Nie ma takiej litery, zostalo Ci " + str(chance) +" szans"
        #return (chance, line, usedLetters)
        return {"chance": chance, "line" :line, "usedLetters" : usedLetters}




if __name__=="__main__":
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
    while True:
        result = game(word,result["chance"],result["line"],result["usedLetters"])


