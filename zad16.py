import random
import string

passWord = []

def password_generator():
    opt = raw_input("Wygenerowac haslo silne czy slabe [s/w]: ")
    if opt == "s":
        for i in range(1,4):
            lowerLetter = "".join(random.choice(string.ascii_lowercase))
            upperLetter = "".join(random.choice(string.ascii_uppercase))
            digit = "".join(random.choice(string.digits))
            symbols = "".join(random.choice(":.,?!$*)(#@%&\[]"))
            passWord.append(lowerLetter + upperLetter + digit +symbols)
            items = ''.join(passWord)
        print ''.join(random.sample(items, len(items)))
        return ''.join(random.sample(items, len(items)))
    else:
        word = ["rzym","kot","klon","krowa","mysz","rower","szkola","lis", "mama", "komputer",
                "jesion", "morze", "kubek", "karta", "olaf", "lisc"]
        number = ["23","88","19","70","12","65"]
        wordUpper = random.choice(word)
        wordLower = random.choice(word)
        randNumber = random.choice(number)
        if wordLower == wordUpper:
            wordUpper = random.choice(word)
            wordLower = random.choice(word)
            print wordUpper.upper() + wordLower + randNumber
            return wordUpper.upper() + wordLower + randNumber
        else:
            print wordUpper.upper() + wordLower + randNumber
            return wordUpper.upper() + wordLower + randNumber

def main():
    password_generator()

main()