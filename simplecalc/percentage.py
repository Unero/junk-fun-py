#!/usr/bin/python3.8
# Calculate result from Percentage


def percentage(n, total):
    result = (n/100) * total
    print("Result from {}% in {} is {}".format(n, total, result))


if __name__ == '__main__':
    n = int(input("Enter your Percentage: "))
    total = int(input("Enter your total ammount: "))
    percentage(n, total)
