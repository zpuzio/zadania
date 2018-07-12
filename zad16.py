import random

a = []
b = []
c = []

def password_generator():
    opt = raw_input("Wygenerowac haslo silne czy slabe [s/w]: ")
    if opt == "s":

        for i in range(1,5):
            a.append(random.choice("abcdefghijkmnoprstuwxyz"))
            result = "".join(a)

        r1 = random.sample(xrange(100),3)

        for i in range(1,4):
            b.append(random.choice("abcdefghijkmnoprstuwxyz"))
            c.append(random.choice(":.,?!$*)(#@%&\[]"))
            r2 = "".join(c)
            r = "".join(b)
            r=r.upper()

        items = result + r + str(r1[1])+r2+str(r1[0])
        print ''.join(random.sample(items, len(items))) #shuffle strings
    else:
        word = ["rzym","kot","klon","krowa","mysz","rower","szkola","lis"]
        wordd = ["mama", "komputer", "jesion", "morze", "kubek", "karta", "olaf", "lisc"]
        number = ["23","88","19","70","12","65"]
        w1 = random.choice(word)
        w2 = random.choice(wordd)
        n1 = random.choice(number)
        print w1+w2.upper()+n1

def main():
    password = password_generator()

main()