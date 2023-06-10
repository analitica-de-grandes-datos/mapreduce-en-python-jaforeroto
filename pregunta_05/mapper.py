#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

for line in sys.stdin:
    line = line.strip()
    if line:
        columns = line.split()
        if len(columns) >= 2:
            date = columns[1].strip()
            month = date.split("-")[1].strip()
            print(f"{month}\t1")
