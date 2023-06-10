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
    # Emite el atributo "purpose" como clave y el monto del crédito "amount" como valor
    purpose = row[3]
    amount = row[4]
    print(f"{purpose}\t{amount}")
