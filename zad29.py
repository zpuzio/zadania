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
        horizontal(size)

def winner(matrix):

    vertical0 = [matrix[i][0] for i in range(0,3)]
    vertical1 = [matrix[i][1] for i in range(0,3)]
    vertical2 = [matrix[i][2] for i in range(0,3)]

    vertical = [vertical0, vertical1, vertical2]

    if (len(set(matrix[0])) == 1 and matrix[0][0]  == "X") or \
            (len(set(matrix[1])) == 1 and matrix[1][0] == "X") or \
            (len(set(matrix[2])) == 1 and matrix[2][0] == "X"):
        print ("Wygrywa 1")
        exit()
    elif (len(set(matrix[0])) == 1 and matrix[0][0] == "O") or \
            (len(set(matrix[1])) == 1 and matrix[1][0] == "O") or \
            (len(set(matrix[2])) == 1 and matrix[2][0] == "O"):
        print ("wygrywa 2")
        exit()
    elif (len(set(vertical[0])) == 1 and vertical[0][0] == "X" ) or \
            (len(set(vertical[1])) == 1 and vertical[1][0] == "X") or \
            (len(set(vertical[2])) == 1 and vertical[2][0] == "X"):
       print ("Wygrywa 1")
       exit()
    elif (len(set(vertical[0])) == 1 and vertical[0][0] == "O") or \
            (len(set(vertical[1])) == 1 and vertical[1][0] == "O") or \
            (len(set(vertical[2])) == 1 and vertical[2][0] == "O"):
       print ("wygrywa 2")
       exit()
    elif matrix[0][0] == matrix[1][1]== matrix[2][2]:
        if matrix[0][0] == "X":
            print ("Wygrywa 1")
            exit()
        if matrix[0][0] == "O":
            print ("wygrywa 2")
            exit()
    elif matrix[0][2] == matrix[1][1] == matrix[2][0]:
        if matrix[1][1] == "X":
            print ("Wygrywa 1")
            exit()
        if matrix[1][1] == "O":
            print ("wygrywa 2")
            exit()


def coordinates_player1(game):
    a = " "
    if a not in game[0] and a not in game[1] and a not in game[2]:
        print("Remis")
        exit()
    else:
        user = raw_input("Graczu 1 jaki jest Twoj ruch, podaj go w formacie wiersz,kolumna np 1,2: ")
        user_list = user.split(",")
        user_list = map(int, user_list)
        x = user_list[0] - 1
        y = user_list[1] - 1
        if x > 2 or y > 2:
            print ("Nieprawidlowe wspolrzedne")
            return coordinates_player1(game)
        if game[x][y] == " ":
            game[x][y] = "X"
            board(game)
            #for i in game:
                #print (i)
            winner(game)
        else:
            print ("To pole jest juz zajete")
            return coordinates_player1(game)
        return game

def coordinates_player2(game):
    a = " "
    if a not in game[0] and a not in game[1] and a not in game[2]:
        print ("Remis")
        exit()
    else:
        user = raw_input("Graczu 2 jaki jest Twoj ruch, podaj go w formacie wiersz,kolumna np 1,2: ")
        user_list = user.split(",")
        user_list = map(int, user_list)
        x = user_list[0] - 1
        y = user_list[1] - 1

        if x > 2 or y > 2:
            print ("Nieprawidlowe wspolrzedne")
            return coordinates_player2(game)
        if game[x][y] == " ":
            game[x][y] = "O"
            board(game)
            #for i in game:
               # print (i)
            winner(game)
        else:
            print ("To pole jest juz zajete")
            return coordinates_player2(game)
        return game

if __name__=="__main__":
    #game = [[0,0,0],[0,0,0],[0,0,0]]
    game = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    board(game)
   # for i in game:
       # print(i)
    while True:
        result = coordinates_player1(game)
        game = coordinates_player2(result)
"""
if __name__=="__main__":


    game = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    size = len(game)
    horizontal(size)
    for x in range(0,3):
        for y in range(0,3):
            print( "| " + str(game[x][y]), end =  "| ")
        print()
        horizontal(size)
"""