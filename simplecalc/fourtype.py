"""
4 Format @ 1 Input

1. Decimal - Base 10
2. Octal - Base 8
3. Hexadecimal(Caps) - Base 16
4. Binary - 0 1

Example:
Input: 10
Output:
   1    1    1    1
   2    2    2   10
   3    3    3   11
   4    4    4  100
   5    5    5  101
   6    6    6  110
   7    7    7  111
   8   10    8 1000
   9   11    9 1001
  10   12    A 1010
"""

def print_formatted(number):
    width = len("{0:b}".format(number))
    for i in range(1, number+1):
        print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=width))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)