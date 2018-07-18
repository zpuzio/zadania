import itertools
import random

iterables = [ [0,1,2], [0,1,2], [0,1,2] ]
elements = [list(iterable) for iterable in itertools.product(*iterables)]
matrix = [random.choice(elements) for i in range(0,3)]
vertical0 = [matrix[i][0] for i in range(0,3)]
vertical1 = [matrix[i][1] for i in range(0,3)]
vertical2 = [matrix[i][2] for i in range(0,3)]
for i in matrix:
    print i

vertical = [vertical0, vertical1, vertical2]

if (len(set(matrix[0])) == 1 and matrix[0][0]  == 1) or \
        (len(set(matrix[1])) == 1 and matrix[1][0] == 1) or \
        (len(set(matrix[2])) == 1 and matrix[2][0] == 1):
    print "Wygrywa 1"
elif (len(set(matrix[0])) == 1 and matrix[0][0] == 2) or \
        (len(set(matrix[1])) == 1 and matrix[1][0] == 2) or \
        (len(set(matrix[2])) == 1 and matrix[2][0] == 2):
    print "wygrywa 2"
elif (len(set(vertical[0])) == 1 and vertical[0][0] == 1 ) or \
        (len(set(vertical[1])) == 1 and vertical[1][0] == 1) or \
        (len(set(vertical[2])) == 1 and vertical[2][0] == 1):
   print "Wygrywa 1"
elif (len(set(vertical[0])) == 1 and vertical[0][0] == 2) or \
        (len(set(vertical[1])) == 1 and vertical[1][0] == 2) or \
        (len(set(vertical[2])) == 1 and vertical[2][0] == 2):
   print "wygrywa 2"
elif matrix[0][0] == matrix[1][1]== matrix[2][2]:
    if matrix[0][0] == 1:
        print "Wygrywa 1"
    if matrix[0][0] == 2:
        print "wygrywa 2"
elif matrix[0][2] == matrix[1][1] == matrix[2][0]:
    if matrix[1][1] == 1:
        print "Wygrywa 1"
    if matrix[1][1] == 2:
        print "wygrywa 2"
else:
    print "remis"
"""
if len(set(matrix[0])) == 1 or len(set(matrix[1])) == 1 or len(set(matrix[2])) == 1:
    if matrix[0][0]  == 1 or matrix[1][0] == 1 or matrix[2][0] == 1:
        print "Wygrywa 1"
    elif matrix[0][0] == 2 or matrix[1][0] == 2 or matrix[2][0] == 2:
        print "wygrywa 2
elif len(set(vertical[0])) == 1 or len(set(vertical[1])) == 1 or len(set(vertical[2])) == 1:
    if vertical[0][0] == 1 or vertical[1][0] == 1 or vertical[2][0] == 1:
        print "Wygrywa 1"
    elif vertical[0][0] == 2 or vertical[1][0] == 2 or vertical[2][0] == 2:
        print "wygrywa 2"
elif matrix[0][0] == matrix[1][1]== matrix[2][2]:
    if matrix[0][0] == 1:
        print "Wygrywa 1"
    if matrix[0][0] == 2:
        print "wygrywa 2"
elif matrix[0][2] == matrix[0][0] == matrix[2][0]:
    if matrix[0][0] == 1:
        print "Wygrywa 1"
    if matrix[0][0] == 2:
        print "wygrywa 2"

else:
    print "remis"
"""