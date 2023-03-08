import time


def measure_time(function_name):
    start_time = time.time()
    result = function_name()
    print(f"{function_name.__name__}: Done in {(time.time() - start_time) * 1000} ms")
    return result
