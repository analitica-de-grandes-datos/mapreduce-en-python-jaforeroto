#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

current_key = None
count = 0

for line in sys.stdin:
    line = line.strip()
    if line:
        key_value = line.split(",")
        if len(key_value) >= 2:
            key = key_value[0].strip()
            value = int(key_value[1].strip())
            if current_key is None:
                current_key = key
            if key == current_key:
                count += value
            else:
                print(f"{current_key},{count}")
                current_key = key
                count = value

# Imprimir el último par clave-valor
if current_key is not None:
    print(f"{current_key},{count}")