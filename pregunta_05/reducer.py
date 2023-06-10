#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

current_month = None
count = 0

for line in sys.stdin:
    line = line.strip()
    if line:
        month, value = line.split("\t")
        if current_month is None:
            current_month = month
        if month == current_month:
            count += int(value)
        else:
            print(f"{current_month}\t{count}")
            current_month = month
            count = int(value)

# Imprimir el último mes y su cantidad de registros
if current_month is not None:
    print(f"{current_month}\t{count}")
