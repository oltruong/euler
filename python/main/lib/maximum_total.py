import copy
import time


def find_maximum_total_iterative_copy(values: list[list[int]]):
    maximum_values = copy.deepcopy(values)
    for idx, value_line in enumerate(values):
        if idx > 0:
            for index, value in enumerate(values[idx]):
                if index == 0:
                    maximum_values[idx][index] = maximum_values[idx - 1][index] + value
                elif index == len(values[idx]) - 1:
                    maximum_values[idx][index] = maximum_values[idx - 1][index - 1] + value
                else:
                    maximum_values[idx][index] = max(
                        maximum_values[idx - 1][index - 1] + value,
                        maximum_values[idx - 1][index] + value,
                    )
    return max(maximum_values[len(maximum_values) - 1])


def find_maximum_total_iterative_matrix(values: list[list[int]]):
    maximum_values = [[] for _ in range(len(values))]
    for idx, value_line in enumerate(values):
        if idx == 0:
            maximum_values[0].append(value_line[0])
        else:
            for index, value in enumerate(values[idx]):
                if index == 0:
                    maximum_values[idx].append(maximum_values[idx - 1][index] + value)
                elif index == len(value_line) - 1:
                    maximum_values[idx].append(maximum_values[idx - 1][index - 1] + value)
                else:
                    maximum_values[idx].append(max(
                        maximum_values[idx - 1][index - 1] + value,
                        maximum_values[idx - 1][index] + value,
                    ))
    return max(maximum_values[len(maximum_values) - 1])


def find_maximum_total_iterative(values: list[list[int]]):
    maximum_values = []
    for value_line in values:
        if len(value_line) == 1:
            maximum_values = value_line
        else:
            new_maximum_values = []
            for index, value in enumerate(value_line):
                if index == 0:
                    new_maximum_values.append(maximum_values[index] + value_line[index])
                elif index == len(maximum_values):
                    new_maximum_values.append(maximum_values[index - 1] + value_line[index])
                else:
                    new_maximum_values.append(max([maximum_values[index + i] + value_line[index] for i in [-1, 0]]))

            maximum_values = new_maximum_values
    return max(maximum_values)

def find_maximum_total_recursive_init(values: list[list[int]] ):
    return find_maximum_total_recursive(1,values[0],values)

def find_maximum_total_recursive(current_index:int,current_values: list[int], values: list[list[int]], ):
    if current_index == len(values):
        return max(current_values)
    else:
        new_values = []
        for index, value in enumerate(values[current_index]):
            if index == 0:
                new_values.append(current_values[index] + values[current_index][index])
            elif index == len(current_values):
                new_values.append(current_values[index - 1] + values[current_index][index])
            else:
                new_values.append(max([current_values[index + i] + values[current_index][index] for i in [-1, 0]]))
        return find_maximum_total_recursive(current_index + 1, new_values,values, )


def find_maximum_total(values: list[list[int]]) -> int:
    result0 = time_find_maximum(find_maximum_total_iterative, values, "Iterative")
    result1 = time_find_maximum(find_maximum_total_iterative_copy, values, "Iterative Copy")
    result2 = time_find_maximum(find_maximum_total_iterative_matrix, values, "Iterative Matrix")
    result3 = time_find_maximum(find_maximum_total_recursive_init, values, "Recursive")
    assert result0 == result1
    assert result0 == result2
    assert result0 == result3
    return result0


def time_find_maximum(find_method, values, description):
    st = time.time()
    result = find_method(values)
    print(f"{description} Done in  {(time.time() - st) * 1000} ms")
    return result
