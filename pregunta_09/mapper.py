#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

# Definir una lista para almacenar los registros
records = []

# Leer los registros de la entrada estándar
for line in sys.stdin:
    # Eliminar espacios en blanco y dividir la línea en campos
    fields = line.strip().split()

    # Extraer los valores relevantes
    letter = fields[0]
    date = fields[1]
    value = int(fields[2])

    # Agregar el registro a la lista
    records.append((value, letter, date))

# Enviar los registros al reducer
for record in records:
    sys.stdout.write(f"{record[1]}\t{record[2]}\t{record[0]}\n")
