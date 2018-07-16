import random

def cows_bulls(userDigit,randDigit):
    cows = 0
    bulls = 0
    randDigit = map(int, str(randDigit)) #zamieniam int na liste
    userDigit = map(int, str(userDigit))
    for i in range(len(randDigit)):
        if randDigit[i] in userDigit and randDigit[i] != userDigit[i]:
            bulls += 1
        if randDigit[i] == userDigit[i]:
            cows += 1

    return {'cows': cows, 'bulls': bulls}

if __name__=="__main__":
    print "Welcome to Cows and Bulls Game!"
    rand = random.randint(1000, 9999)
    resultValues = 0
    countCows = 0
    countBulls = 0
    i = 0
    while countCows != 4:
        user = int(raw_input("Enter 4 digit number: "))
        result = cows_bulls(user,rand)

        resultValues = result.values()
        countCows = resultValues[0]
        countBulls = resultValues[1]
        i += 1
        print str(countCows) + " cows  " +str(countBulls) + " bulls"
        if countCows == 4:
            print "Wygrales, zajelo Ci to " + str(i) + " prob!"