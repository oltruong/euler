def get_divisors_per_number(param):
    divisor = 1
    sum_of_divisors = 0

    while divisor <= param / 2:
        if param % divisor == 0:
            sum_of_divisors += divisor
        divisor += 1

    return sum_of_divisors


def get_problem21():
    result = 0
    known_numbers = set()

    for i in range(1, 10001):
        if i not in known_numbers:
            divisors = get_divisors_per_number(i)
            if i != divisors and get_divisors_per_number(divisors) == i:
                result += i
                result += divisors
                known_numbers.add(i)
                known_numbers.add(divisors)

    return result
