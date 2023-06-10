#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

lst = []

for row in sys.stdin:
    split_row = row.strip().split(",")
    if len(split_row) == 3:
        lst.append((split_row[0], split_row[1], int(split_row[2])))

# Ordena por letra en orden ascendente y valor en orden ascendente
lst.sort(key=lambda x: (x[0], x[2]))

for key in lst:
    sys.stdout.write(key[0] + "   " + key[1] + "   " + str(key[2]) + "\n")
