#p1 = raw_input("Gracz1, Papier, kamien czy nozyczki... ")
#p2 = raw_input("Gracz2, Papier, kamien czy nozyczki... ")

while True:
    print "Jesli chcesz zakonczyc gre wpisz stop"
    p1 = raw_input("Gracz1, Papier, kamien czy nozyczki... ")
    if p1 == "stop":
        break
    p2 = raw_input("Gracz2, Papier, kamien czy nozyczki... ")
    if p1 == "stop" or p2 == "stop":
        break
    elif p1 == "nozyczki" and p2 == "kamien":
        print "Gracz2 wygral!"
    elif p2 == "nozyczki" and p1 == "kamien":
        print "Gracz1 wygral!"
    elif p1 == "nozyczki" and p2 == "papier":
        print "Gracz1 wygral!"
    elif p2 == "nozyczki" and p1 == "papier":
        print "Gracz2 wygral!"
    elif p1 == "papier" and p2 == "kamien":
        print "Gracz1 wygral!"
    elif p2 == "papier" and p1 == "kamien":
        print "Gracz2 wygral!"