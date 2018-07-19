from __future__ import print_function
symbol1 = "X"
symbol2 = "o"
def horizontal(size):
    print(" ---  " * size)

def board(game):
    size = len(game)
    horizontal(size)
    for x in range(0, 3):
        for y in range(0, 3):
            print("| " + str(game[x][y]), end=" | ")
        print()
        horizontal(size)
def winner(rows):
    import numpy as np
    cols = list(zip(*rows))  # kolumny
    diagonals = [np.diag(rows).tolist(), np.diag(np.rot90(rows)).tolist()]  # przekatna_dlugosc

    for i in range(len(cols)):
        rzad_dlugosc = len(set(rows[i]))
        kolumna_dlugosc = len(set(cols[i]))
        if rzad_dlugosc == 1:
            if rows[i][0] == symbol1:
                print("Wygrywa gracz 1")
                exit()
            elif rows[i][0] == symbol2:
                print ("Wygrywa gracz 2")
                exit()
        elif kolumna_dlugosc == 1:
            if cols[i][0] == symbol1:
                print("Wygrywa gracz 1")
                exit()
            elif cols[i][0] == symbol2:
                print ("Wygrywa gracz 2")
                exit()
        else:
            for j in range(len(diagonals)):
                przekatna_dlugosc = len(set(diagonals[j]))
                if przekatna_dlugosc == 1:
                    if diagonals[j][0] == symbol1:
                        print ("Wygrywa gracz 1")
                        exit()
                    elif diagonals[j][0] == symbol2:
                        print ("Wygrywa gracz 2")
                        exit()

def userInput(userIn):
    userList = userIn.split(",")
    userList = map(int, userList)
    row = userList[0] - 1
    col = userList[1] - 1
    return (row, col)

def wrong_coordinates(x,y,game):
    if x > 2 or y > 2:
        print ("Nieprawidlowe wspolrzedne")
        return False
    elif game[x][y] != 0:
        print ("To pole jest zajete")
        return False
    else:
        return True

def remis(game):
    zero = 0
    if zero not in game[0] and zero not in game[1] and zero not in game[2]:
        print ("Remis")
        exit()

def coordinates_player1(game):
    remis(game)
    userIn = raw_input("Graczu 1 jaki jest Twoj ruch, podaj go w formacie wiersz,kolumna_dlugosc np 1,2: ")
    input_user = userInput(userIn)
    x = input_user[0]
    y = input_user[1]
    checkCoordinates = wrong_coordinates(x,y,game)
    while checkCoordinates == False:
        userIn = raw_input("Graczu 1 jaki jest Twoj ruch, podaj go w formacie wiersz,kolumna_dlugosc np 1,2: ")
        input_user = userInput(userIn)
        x = input_user[0]
        y = input_user[1]
        checkCoordinates = wrong_coordinates(x, y, game)
    if game[x][y] == 0:
        game[x][y] = symbol1
        board(game)
        winner(game)
    return game

def coordinates_player2(game):
    remis(game)
    userIn = raw_input("Graczu 2 jaki jest Twoj ruch, podaj go w formacie wiersz,kolumna_dlugosc np 1,2: ")
    input_user = userInput(userIn)
    x = input_user[0]
    y = input_user[1]

    checkCoordinates = wrong_coordinates(x, y, game)
    while checkCoordinates == False:
        userIn = raw_input("Graczu 2 jaki jest Twoj ruch, podaj go w formacie wiersz,kolumna_dlugosc np 1,2: ")
        input_user = userInput(userIn)
        x = input_user[0]
        y = input_user[1]
        checkCoordinates = wrong_coordinates(x, y, game)
    if game[x][y] == 0:
        game[x][y] = symbol2
        board(game)
        winner(game)
    return game

if __name__=="__main__":
    game = [[0,0,0],[0,0,0],[0,0,0]]
    # game = [[" " ," "," "],[" " ," "," "],[" " ," "," "]]
    board(game)
    while True:
        result = coordinates_player1(game)
        game = coordinates_player2(result)