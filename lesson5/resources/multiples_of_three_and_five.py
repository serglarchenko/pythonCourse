"""
These are different solutions of "Task 5: Multiples of 3 and 5. Find the best algorithm"

Let's find out which of the proposed algorithms is the most effective
"""

import multiprocessing
from lesson4.task_4_2 import Timer

N = 300000000


def simple_iteration():
    res = 0
    for i in range(N):
        if i % 3 == 0 or i % 5 == 0:
            res += i
    return print(f"{res} simple_iteration completed")


def several_for_loops():
    res = 0
    for i in range(3, N, 3):
        res += i
    for i in range(5, N, 5):
        res += i
    for i in range(15, N, 15):
        res -= i
    return print(f"{res} several_for_loops completed")


def iterate_over_fifteen():
    range_diff = [0, 3, 5, 6, 9, 10, 12]
    res = 0
    for i in range(0, N, 15):
        for d in range_diff:
            v = i + d
            if v >= N:
                break
            res += v
    return print(f"{res} iterate_over_fifteen completed")


def math_formula():
    upper = N - 1
    threes = int(3 * (upper / 3) * ((upper / 3) + 1) / 2)
    fives = int(5 * (upper / 5) * ((upper / 5) + 1) / 2)
    fifteens = int(15 * (upper / 15) * ((upper / 15) + 1) / 2)
    res = threes + fives - fifteens
    return print(f"{res} math_formula completed")


def run_all_calculations_in_parallel():
    # Use multiprocessing library to run all above functions in parallel
    # Print execution time of each function

    with Timer('simple_iteration ->'):
        p = multiprocessing.Process(target=simple_iteration)
        p.name.title()
        p.start()
        p.join()
    with Timer('several_for_loops ->'):
        p2 = multiprocessing.Process(target=several_for_loops)
        p2.start()
        p2.join()
    with Timer('iterate_over_fifteen ->'):
        p3 = multiprocessing.Process(target=iterate_over_fifteen)
        p3.start()
        p3.join()
    with Timer('math_formula ->'):
        p4 = multiprocessing.Process(target=math_formula)
        p4.start()
        p4.join()


if __name__ == '__main__':
    run_all_calculations_in_parallel()




