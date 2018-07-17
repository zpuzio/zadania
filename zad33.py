def birthday_dictionary():
    birthday = {
        "Albert Einstein": "14/03/1879",
        "Ada Lovelace" : "10/12/1815",
        "Benjamin Franklin": "17/01/1706"

    }
    print  "Welcome to the birthday dictionary. We know the birthdays of:"
    for name in birthday.keys():
        print name
    userInput = raw_input("Who's birthday do you want to look up? ")
    if userInput not in birthday:
        print "Not in birthday dictionary"
    else:
        print userInput + " birthday is " + birthday[userInput]



if __name__ == "__main__":
    birthday_dictionary()

