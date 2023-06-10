#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

for line in sys.stdin:
    line = line.strip()
    columns = line.split(",")
    key = columns[1]
    value = line
    print(f"{key}\t{value}")
