import random

def cows_bulls(x):

        count = [0,0]
        z = random.randint(1000,9999)
        z = map(int, str(z)) #zamieniam int na liste
        x = map(int, str(x))
        for i in range(0,len(z)):
                if z[i] == x[i]:
                    count[0] += 1
                else:
                    count[1] += 1
        return count



if __name__=="__main__":
    print "Welcome to Cows and Bulls Game!"

    #print cows_bulls(y)
    c = 0
    i = 0
    while c !=2:
        y = int(raw_input("Enter 4 digit number: "))
        result = cows_bulls(y)

        c = result[0]
        i +=1
        print str(result[0]) + " cows", str(result[1]) + " bulls"
        if c == 2:
            print "Wygrales, zajelo Ci to " + str(i) + " prob!"