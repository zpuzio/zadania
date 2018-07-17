import json

birthday = {
    "Albert Einstein": "14/03/1879",
    "Ada Lovelace": "10/12/1815",
    "Benjamin Franklin": "17/01/1706"

}
with open('birthday.json', 'r') as f:
    birthday = json.load(f)
def birthdayAdd():
    addName = raw_input("Kogo chcesz dodac: ")
    addDate = raw_input("Kiedy sie urodzil: ")
    birthday[addName] = addDate
    with open("birthday.json", "w") as file:
        json.dump(birthday, file)
    #new = birthday.update({person: date})
def birthdayFind():
    findPerson = raw_input("Kogo szukasz: ")
    if findPerson in birthday:
        print "{} urodzila sie {}".format(findPerson, birthday[findPerson])
    else:
        print "Nie znaleziono"
def birthdayList():
    for name in birthday.keys():
        print name
if __name__ == "__main__":
    while True:
        user = raw_input("Co chcesz zrobic dodac element, znalezc, wypisac wszsytkie elementy czy zakonczyc [d/z/w/s]: ")
        if user == "d":
            birthdayAdd()
        elif user == "z":
            birthdayFind()
        elif user == "w":
            birthdayList()
        else:
            exit()
