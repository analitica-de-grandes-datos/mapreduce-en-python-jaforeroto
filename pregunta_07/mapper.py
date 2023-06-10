#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

for row in sys.stdin:
    split_row = row.strip().split("   ")
    sys.stdout.write(split_row[0] + "," +
                     split_row[1] + "," + split_row[2] + "\n")
