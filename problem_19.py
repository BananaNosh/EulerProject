import datetime
import math
from tools import read_input_as_string
import itertools
prob12_17 = __import__('problem_12-17')
prob1_7 = __import__('problem_1-7')


# prob 19
def all_sundays(start, end):
    sundays = []
    date = start
    while date != end:
        if date.isoweekday() == 7:
            sundays.append(date)
        date += datetime.timedelta(1)
    return sundays


# prob 21
def find_amicables(limit):
    found = {}
    summed = 0
    for i in range(limit):
        if i in found:
            continue
        friend = amicable_friend(i)
        if friend:
            found[friend] = i
            summed += i + friend
    return summed


def amicable_friend(number):
    d = sum(all_divisors(number))
    if number == sum(all_divisors(d)) and d != number:
        return d
    return None


def all_divisors(number):
    divisors = []
    for i in range(number // 2, 0, -1):
        if number % i == 0:
            divisors.append(i)
    return divisors


# prob 22
def name_scores(names):
    names = sorted(names)
    scores = []
    for i, name in enumerate(names):
        name_score = 0
        for l in name.strip("\""):
            letter_score = ord(l) - 64
            name_score += letter_score
        scores.append(name_score * (i+1))
    return scores


# prob 23
def find_abundant_numbers(limit):
    numbers = []
    for i in range(1, limit+1):
        abundant = sum(all_divisors(i)) > i
        if abundant:
            numbers.append(i)
    return numbers


def find_numbers_not_formed_by_abundant(limit):
    abundant = find_abundant_numbers(limit)
    formed_by_abundant = set()
    for i, ab1 in enumerate(abundant):
        for ab2 in abundant[i:]:
            formed_by_abundant.add(ab1 + ab2)
    print(len(abundant), len(formed_by_abundant))
    numbers = []
    for i in range(1, limit+1):
        if i not in formed_by_abundant:
            numbers.append(i)
    return numbers


# prob 24
def all_permutations(digits=None):
    if digits is None:
        digits = [i for i in range(10)]
    digits = [str(i) for i in digits]
    perm = itertools.permutations(digits)
    return [int("".join(p)) for p in perm]




if __name__ == '__main__':
    # print(len([sun for sun in all_sundays(datetime.date(1901, 1, 1), datetime.date(2000, 12, 31)) if sun.day == 1]))
    # print(prob12_17.digit_sum(math.factorial(100)))  # prob 20
    # print(find_amicables(10000))
    # print(sum(name_scores(read_input_as_string(22).split(","))))
    # numbers = find_numbers_not_formed_by_abundant(28123)
    print(all_permutations()[999990:1000010])
