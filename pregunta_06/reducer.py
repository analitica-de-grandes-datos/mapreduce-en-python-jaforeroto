#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

current_letter = None
max_value = float("-inf")
min_value = float("inf")

for line in sys.stdin:
    line = line.strip()
    if line:
        letter, value, _ = line.split("\t")
        if current_letter is None:
            current_letter = letter
        if letter == current_letter:
            value = float(value)
            max_value = max(max_value, value)
            min_value = min(min_value, value)
        else:
            if current_letter != None:
                print(f"{current_letter}\t{max_value:.1f}\t{min_value:.1f}")
            current_letter = letter
            max_value = float("-inf")
            min_value = float("inf")
            value = float(value)
            max_value = max(max_value, value)
            min_value = min(min_value, value)

# Imprimir la última letra con sus valores máximo y mínimo
if current_letter is not None:
    print(f"{current_letter}\t{max_value:.1f}\t{min_value:.1f}")
