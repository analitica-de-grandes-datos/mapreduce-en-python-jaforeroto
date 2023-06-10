#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
from collections import defaultdict

elements = defaultdict(list)

for line in sys.stdin:
    letter, number = line.strip().split('*')
    elements[letter].append(int(number))

for letter, numbers in elements.items():
    numbers = ','.join(str(number) for number in sorted(numbers))
    print(f"{letter}\t{numbers}")
