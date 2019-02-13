from tools import read_input_as_string
from functools import reduce
import operator
from collections import deque
prob1_7 = __import__('problem_1-7')
import numpy as np


# prob 8
def find_greatest_adjacent_product(string, n):
    current_numbers = deque([int(d) for d in string[:n]])
    product = prod(current_numbers)
    greatest = (product, list(current_numbers))
    for s in string[n+1:]:
        try:
            d = int(s)
            left_most = current_numbers[0]
            current_numbers.popleft()
            current_numbers.append(d)
            if left_most == 0:
                product = prod(current_numbers)
            else:
                product //= left_most
                product *= d
            if product > greatest[0]:
                greatest = (product, list(current_numbers))
        except ValueError:
            continue
    return greatest


def prod(numbers):
    return reduce(operator.mul, numbers, 1)


# prob 9
def find_phyt_triplet(sum, limit=1):
    possible_trips = []
    for greatest in range(sum // 3 + 1, sum-2):
        for second in range((sum - greatest + 1) // 2, greatest):
            third = sum - greatest - second
            if third < 0:
                break
            if third**2 + second**2 == greatest**2:
                possible_trips.append((third, second, greatest))
                if len(possible_trips) == limit:
                    return possible_trips
    return possible_trips


# prob 10
def sum_of_prims_below(limit):
    result = 0
    for i in range(2, limit):
        print(i, end="")
        if len(prob1_7.factorize(i)) == 1:
            result += i
            print(" ok", end="")
        print("")
    return result


# prob 11
def greatest_product_from_grid(grid, n=4):
    print(grid)
    greatest = 0
    for y, row in enumerate(grid):
        for x, field in enumerate(row):
            shifts = [[0, 1], [1, 0], [1, 1], [-1, 1]]
            for x_shift, y_shift in shifts:
                result = 1
                for i in range(n):
                    try:
                        result *= grid[y + i*y_shift, x + i*x_shift]
                    except IndexError as e:
                        result = 0
                        break
                if result > greatest:
                    greatest = result
    return greatest


if __name__ == '__main__':
    input_8 = read_input_as_string(8)
    print(find_greatest_adjacent_product(input_8, 13))
    triplet = find_phyt_triplet(1000)
    print(prod(triplet[0]))
    # print(sum_of_prims_below(2000000))
    grid = np.genfromtxt("./inputs/11_input.txt", dtype=np.int)
    print(greatest_product_from_grid(grid))
