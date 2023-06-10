#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

for line in sys.stdin:
    line = line.strip()
    if line:
        columns = line.split()
        if len(columns) >= 3:
            letter = columns[0].strip()
            value = float(columns[2].strip())
            print(f"{letter}\t{value}\t{value}")
