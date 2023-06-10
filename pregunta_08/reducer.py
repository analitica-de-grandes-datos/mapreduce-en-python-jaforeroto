#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

dict_count = {}
dict_sum = {}

for line in sys.stdin:
    letter, value = line.strip().split("\t")
    value = int(value)

    dict_count.setdefault(letter, 0)
    dict_sum.setdefault(letter, 0)

    dict_count[letter] += 1
    dict_sum[letter] += value

for letter in dict_count.keys():
    total_sum = dict_sum[letter]
    total_count = dict_count[letter]
    average = total_sum / total_count

    sys.stdout.write(f"{letter}\t{total_sum:.1f}\t{average}\n" if average.is_integer(
) else f"{letter}\t{total_sum:.1f}\t{average}\n")
