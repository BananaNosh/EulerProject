import sys
prob1_7 = __import__('problem_1-7')
from collections import Counter


# prob 12
def first_triangle_with_more_as_n_divisors(limit):
    def check_for_n(current_factors):
        number_of_all_divs = 1
        for _, count in current_factors.items():
            number_of_all_divs *= (count+1)
        print("number of all divs", number_of_all_divs)
        return number_of_all_divs >= limit

    triangle = 1 + 2
    all_factors = {1: Counter(), 2: Counter([2])}
    for n in range(3, sys.maxsize, 2):
        greatest_div = greatest_divisor(n)
        factors_of_n = all_factors[greatest_div] + Counter([n // greatest_div])
        all_factors[n] = factors_of_n
        n_minus_1_half = (n - 1) // 2
        factors_of_n_minus_1_half = all_factors[n_minus_1_half]
        current_factors = merge_factors(factors_of_n, factors_of_n_minus_1_half)
        print(triangle, current_factors)
        if check_for_n(current_factors):
            return triangle
        triangle += n
        factors_of_n_plus_1_half = all_factors[(n + 1) // 2]
        factors_of_n_plus_1 = factors_of_n_plus_1_half + Counter([2])
        all_factors[n+1] = factors_of_n_plus_1
        current_factors = merge_factors(factors_of_n, factors_of_n_plus_1_half)
        print(triangle, current_factors)
        if check_for_n(current_factors):
            return triangle
        triangle += n + 1

    return None


def merge_factors(counter1, counter2):
    counter1 = counter1.copy()
    for key, count in counter2.items():
        if key not in counter1 or count > counter1[key]:
            counter1[key] = count
    return counter1


def greatest_divisor(odd_number):
    start = odd_number // 2 + (1 if odd_number % 4 == 1 else 0)
    for i in range(start, 0, -2):
        if odd_number % i == 0:
            return i


# prob 13
def sum_big_numbers(lines):
    result = 0
    for line in lines:
        result += int(line)
    return result


# prob 14
def find_longest_collatz(starting_limit):
    found = {1: 1}
    greatest = 0, None
    for i in range(2, starting_limit+1):
        number = i
        sequenz = [number]
        while True:
            if number % 2 == 0:
                number //= 2
            else:
                number = 3*number + 1
            sequenz.append(number)
            if number in found:
                break
        count = found[sequenz[-1]]
        for j in reversed(sequenz[:-1]):
            count += 1
            found[j] = count
        if count > greatest[0]:
            greatest = count, i
    return greatest


# prob 16
def digit_sum(number):
    d_sum = 0
    while number > 0:
        d_sum += number % 10
        number //= 10
    return d_sum


# prob 17
def number_to_string(number):
    one_numbers = ["zero","one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    hundred = "hundred"
    thousand = "thousand"
    if number < 10:
        return one_numbers[number]
    elif number < 20:
        return teens[number-10]
    elif number < 100:
        rest = number % 10
        return tens[number // 10 - 1] + ("-" + number_to_string(rest) if rest > 0 else "")
    elif number < 1000:
        rest = number % 100
        return one_numbers[number // 100] + hundred + (" and " + number_to_string(rest) if rest > 0 else "")
    elif number < 1000000:
        rest = number % 1000
        return number_to_string(number // 1000) + " " + thousand + (" " + number_to_string(rest) if rest > 0 else "")
    else:
        raise AttributeError("Not yet implemented")


def all_numbers_string(start, end):
    total = ""
    for i in range(start, end+1):
        total += number_to_string(i) + " "
    return total.strip()


if __name__ == '__main__':
    # print(first_triangle_with_more_as_n_divisors(500))
    # print(sum_big_numbers(read_input_line_wise(13)))
    # print(find_longest_collatz(1000000))
    print(digit_sum(2**1000))
    result = all_numbers_string(1, 1000).replace(" ", "").replace("-", "")
    print(len(result), result)
    print(number_to_string(342), number_to_string(115))
