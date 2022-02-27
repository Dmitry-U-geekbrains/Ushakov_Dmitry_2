# show_sales.py
import sys


def read_sale(argv):
    program, *ars = argv
    result = str()
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        list_line = f.read().splitlines()
        if len(ars) == 0:
            ars.append(1)
            ars.append(len(list_line))
        elif len(ars) == 1:
            ars.append(len(list_line))
        start = int(ars[0])
        stop = int(ars[1])
        if start == 0 or start > len(list_line) or stop > len(list_line):
            return result
        for el in list_line[start - 1: stop]:
            result += f'{el}\n'
        return result.strip('\n')


if __name__ == '__main__':
    print(read_sale(sys.argv))
