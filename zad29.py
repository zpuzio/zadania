from __future__ import print_function

def horizontal(size):
    print(" --- " * size)

def board(game):
    size = len(game)
    horizontal(size)
    for x in range(0, 3):
        for y in range(0, 3):
            print("| " + str(game[x][y]), end="| ")
        print()
def winner(matrix):

    vertical0 = [matrix[i][0] for i in range(0,3)]
    vertical1 = [matrix[i][1] for i in range(0,3)]
    vertical2 = [matrix[i][2] for i in range(0,3)]

    vertical = [vertical0, vertical1, vertical2]
    p1 = "X"
    p2 = "#"
    if (len(set(matrix[0])) == 1 and matrix[0][0]  == p1) or \
            (len(set(matrix[1])) == 1 and matrix[1][0] == p1) or \
            (len(set(matrix[2])) == 1 and matrix[2][0] == p1):
        print ("Wygrywa gracz 1")
        exit()
    elif (len(set(matrix[0])) == 1 and matrix[0][0] == p2) or \
            (len(set(matrix[1])) == 1 and matrix[1][0] == p2) or \
            (len(set(matrix[2])) == 1 and matrix[2][0] == p2):
        print ("Wygrywa gracz 2")
        exit()
    elif (len(set(vertical[0])) == 1 and vertical[0][0] == p1 ) or \
            (len(set(vertical[1])) == 1 and vertical[1][0] == p1) or \
            (len(set(vertical[2])) == 1 and vertical[2][0] == p1):
       print ("Wygrywa gracz 1")
       exit()
    elif (len(set(vertical[0])) == 1 and vertical[0][0] == p2) or \
            (len(set(vertical[1])) == 1 and vertical[1][0] == p2) or \
            (len(set(vertical[2])) == 1 and vertical[2][0] == p2):
       print ("Wygrywa gracz 2")
       exit()
    elif matrix[0][0] == matrix[1][1]== matrix[2][2]:
        if matrix[0][0] == p1:
            print ("Wygrywa gracz 1")
            exit()
        if matrix[0][0] == p2:
            print ("Wygrywa gracz 2")
            exit()
    elif matrix[0][2] == matrix[1][1] == matrix[2][0]:
        if matrix[1][1] == p1:
            print ("Wygrywa gracz 1")
            exit()
        if matrix[1][1] == p2:
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
    userIn = raw_input("Graczu 1 jaki jest Twoj ruch, podaj go w formacie wiersz,kolumna np 1,2: ")
    input_user = userInput(userIn)
    x = input_user[0]
    y = input_user[1]
    checkCoordinates = wrong_coordinates(x,y,game)
    while checkCoordinates == False:
        userIn = raw_input("Graczu 1 jaki jest Twoj ruch, podaj go w formacie wiersz,kolumna np 1,2: ")
        input_user = userInput(userIn)
        x = input_user[0]
        y = input_user[1]
        checkCoordinates = wrong_coordinates(x, y, game)
    if game[x][y] == 0:
        game[x][y] = "X"
        board(game)
        winner(game)
    return game

def coordinates_player2(game):
    remis(game)
    userIn = raw_input("Graczu 2 jaki jest Twoj ruch, podaj go w formacie wiersz,kolumna np 1,2: ")
    input_user = userInput(userIn)
    x = input_user[0]
    y = input_user[1]

    checkCoordinates = wrong_coordinates(x, y, game)
    while checkCoordinates == False:
        userIn = raw_input("Graczu 2 jaki jest Twoj ruch, podaj go w formacie wiersz,kolumna np 1,2: ")
        input_user = userInput(userIn)
        x = input_user[0]
        y = input_user[1]
        checkCoordinates = wrong_coordinates(x, y, game)
    if game[x][y] == 0:
        game[x][y] = "#"
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