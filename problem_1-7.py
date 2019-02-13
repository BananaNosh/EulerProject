from itertools import chain
from collections import Counter
import sys


# prob 1
def find_multiples(dividers, limit):
    multiples = []
    for i in range(1, limit):
        for d in dividers:
            if i % d == 0:
                multiples.append(i)
                break
    return multiples


# prob 2
def even_fibonaccis(limit):
    even = [2]
    first = 1
    second = 2
    while True:
        first = second + first
        second = first + second
        if first > limit:
            break
        if first % 2 == 0:
            even.append(first)
        if second > limit:
            break
        if second % 2 == 0:
            even.append(second)
    return even


# prob 3
def prim_factors(number):
    not_divisors = set()
    factors = []
    for i in range(2, number // 2):
        if i in not_divisors:
            not_divisors.remove(i)
            continue
        if number % i == 0:
            factors.append(i)
        for j in range(i, (number + 1) // 2, i):
            not_divisors.add(j)
    if len(factors) == 0:
        factors = [1, number]
    return factors


def factorize(n):
    l = []  # Lösungsmenge
    # Auf Teilbarkeit durch 2, und alle ungeraden Zahlen von 3..n/2 testen
    for i in chain([2], range(3, n // 2 + 1, 2)):
        # Ein Teiler kann mehrfach vorkommen (z.B. 4 = 2 * 2), deswegen:
        while n % i == 0:
            l.append(i)
            n = n // i  # "//" ist ganzzahlige Division und entspricht int(n/i)
        if i > n:  # Alle Teiler gefunden? Dann Abbruch.
            break
    if len(l) == 0:
        return [n]
    return l


# prob 4
def is_palindrom(number):
    string = str(number)
    return string[::-1] == string


def find_special_palindrom(divisor_limit):
    for i in range(divisor_limit**2, 9, -1):
        if is_palindrom(i):
            for j in range(divisor_limit, 0, -1):
                if i % j == 0:
                    greater_divisor = i // j
                    if greater_divisor > divisor_limit:
                        break
                    else:
                        return i


# prob 5
def smallest_multiple(numbers):
    all_prim_factors = [Counter(factorize(n)) for n in numbers]
    merged = dict(all_prim_factors[0].items())
    for factors in all_prim_factors[1:]:
        for prim, count in factors.items():
            if prim not in merged or merged[prim] < count:
                merged[prim] = count
    print(merged)
    result = 1
    for prim, count in merged.items():
        result *= prim**count
    return result


# prob 6
def sum_square_difference(n):
    square_sum = n*(n + 1)*(2*n + 1) // 6
    sum_squared = (n*(n+1)//2)**2
    return sum_squared - square_sum


# prob 7
def n_th_prime(n):
    count = 1
    for i in range(2, sys.maxsize):
        if len(factorize(i)) == 1:
            count += 1
            if count == n:
                return i
    raise ValueError("to big numbers")


if __name__ == '__main__':
    multiples = find_multiples([3, 5], 10)
    print(sum(multiples))
    multiples = find_multiples([3, 5], 1000)
    print(sum(multiples), multiples)

    print(sum(even_fibonaccis(4000000)))
    print(factorize(600851475143))
    print(factorize(24))
    # print(prim_factors(600851475143))

    print(find_special_palindrom(999))

    print(smallest_multiple(list(range(1, 21))))

    print(sum_square_difference(100))

    print(n_th_prime(10001))
