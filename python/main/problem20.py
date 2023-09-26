

def get_problem20():
    factorial = get_factorial(100)
    print(factorial)
    result = 0
    for digit in str(factorial):
        result += int(digit)

    return result


def get_factorial(param):
    if param < 1:
        raise ValueError(f"Invalid number {param}")
    elif param == 1:
        return 1
    else:
        return param * get_factorial(param - 1)
