#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

for line in sys.stdin:
    letter, _, value = line.strip().split()
    sys.stdout.write(f"{letter}\t{value}\n")
