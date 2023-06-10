#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

# Lee la entrada de la línea de comandos
input_data = sys.stdin

# Diccionario para almacenar el valor máximo del monto de crédito por cada tipo de destino
max_amounts = {}

# Itera sobre cada línea de entrada
for line in input_data:
    # Elimina los caracteres de nueva línea y divide la línea en clave y valor
    line = line.strip()
    purpose, amount = line.split('\t')

    # Si el tipo de destino ya existe en el diccionario, compara y actualiza el máximo si es necesario
    if purpose in max_amounts:
        max_amounts[purpose] = max(max_amounts[purpose], float(amount))
    # Si el tipo de destino no existe, agrega una nueva entrada al diccionario
    else:
        max_amounts[purpose] = float(amount)

# Imprime el resultado final con el formato esperado
for purpose, max_amount in max_amounts.items():
    print(f"{purpose}\t{int(max_amount)}")
