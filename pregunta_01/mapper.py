#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
import csv

# Lee la entrada de la línea de comandos
input_file = sys.stdin

# Lee el archivo CSV con los datos
data = csv.reader(input_file)

# Itera sobre cada fila del archivo CSV
for row in data:
    # Realiza las operaciones de mapeo aquí
    # Emite el atributo "credit_history" como clave y un valor constante de 1
    credit_history = row[2]
    print(f"{credit_history}\t1")