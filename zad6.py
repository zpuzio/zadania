#Do geese see God
string  = raw_input("Podaj wyraz: ")
n = string.replace(" ", "")
print n
#d = len(string)+1
s = n[::-1]
print s
if n.lower() == s.lower():
    print "Palindrom"
else:
    print "To nie jest palindrom"