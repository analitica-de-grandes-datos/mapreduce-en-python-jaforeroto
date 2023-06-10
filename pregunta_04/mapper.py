#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

for line in sys.stdin:
    line = line.strip()
    if line:
        columns = line.split()
        if len(columns) >= 1:
            key = columns[0].strip()
            print(f"{key},1")
