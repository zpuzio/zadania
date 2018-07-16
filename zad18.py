import random
import itertools
def cows_bulls(userDigit,randDigit):
    cows = 0
    bulls = 0
    userDigit = map(int, str(userDigit))#zamieniam int na liste
    for i in range(len(randDigit)):
        if randDigit[i] == userDigit[i]:
            cows += 1
        elif userDigit[i] in randDigit:
            bulls += 1
    return {'cows': cows, 'bulls': bulls}

if __name__=="__main__":
    print "Welcome to Cows and Bulls Game!"
    rands = []
    iterables = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]
    for t in itertools.product(*iterables):
        rands.append(t)
    rand = list(random.choice(rands))
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