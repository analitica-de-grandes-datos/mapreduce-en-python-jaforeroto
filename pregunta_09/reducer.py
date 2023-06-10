#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

# Definir una lista para almacenar los registros
records = []

# Leer los registros del mapper
for line in sys.stdin:
    # Eliminar espacios en blanco y dividir la línea en campos
    fields = line.strip().split("\t")

    # Extraer los valores relevantes
    letter = fields[0]
    date = fields[1]
    value = int(fields[2])

    # Agregar el registro a la lista
    records.append((letter, date, value))

# Ordenar los registros por el valor en orden ascendente
sorted_records = sorted(records, key=lambda x: x[2])

# Enviar los 6 registros más pequeños a la salida
for record in sorted_records[:6]:
    print(str(record[0]) + "   " + str(record[1]) + "   " + str(record[2]))
