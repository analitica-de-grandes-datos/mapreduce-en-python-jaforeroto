#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

for line in sys.stdin:
    number, letters = line.strip().split('\t')
    letters = letters.replace("'", "").split(',')
    for letter in letters:
        print(f"{letter}*{number}")
