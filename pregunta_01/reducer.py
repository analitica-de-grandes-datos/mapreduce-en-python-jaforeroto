#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

# Lee la entrada de la línea de comandos
input_data = sys.stdin

# Diccionario para almacenar la cantidad de registros por cada tipo de historial de crédito
credit_history_counts = {}

# Itera sobre cada línea de entrada
for line in input_data:
    # Elimina los caracteres de nueva línea y divide la línea en clave y valor
    line = line.strip()
    credit_history, count = line.split('\t')

    # Si el tipo de historial de crédito ya existe en el diccionario, incrementa el contador
    if credit_history in credit_history_counts:
        credit_history_counts[credit_history] += int(count)
    # Si el tipo de historial de crédito no existe, agrega una nueva entrada al diccionario
    else:
        credit_history_counts[credit_history] = int(count)

# Imprime el resultado final
for credit_history, count in credit_history_counts.items():
    print(f"{credit_history}\t{count}")
