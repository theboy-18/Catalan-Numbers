from functools import reduce


def nth_catalan(n):
    numerator = reduce((lambda x, y: x*y), [numbers for numbers in range(2, 4*n-1, 4)])
    denominator = reduce((lambda x, y: x*y), [numbers for numbers in range(1, n+2)])
    catalan_number = int(numerator/denominator)
    print(f'The {n}th Catalan number is {catalan_number}')









