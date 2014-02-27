import sys
import random
import time

def brute_force(A):
    max_sum = 0

    for idx, i in enumerate(A):
        this_sum = 0
        for j in A[idx:]:
            this_sum += j
            max_sum = max(max_sum, this_sum)

    return max_sum 

def divide_conquer(A):
    midpoint = int(len(A) / 2)

    if len(A) == 0:
        return 0
    elif len(A) == 1:
        return max(0, A[0])

    max_left = divide_conquer(A[:midpoint])
    max_right = divide_conquer(A[midpoint:])

    cur_sum = 0
    left_sum = 0
    for x in reversed(A[:midpoint]):
        cur_sum += x
        if cur_sum > left_sum:
            left_sum = cur_sum

    cur_sum = 0
    right_sum = 0
    for x in A[midpoint:]:
        cur_sum += x
        if cur_sum > right_sum:
            right_sum = cur_sum

    return max(max_left, max_right, left_sum + right_sum)

def dynamic_programming(A):
    m = [0] * len(A)
    m[0] = max(0, A[0])
    best_sum = m[0]
    for i, x in enumerate(A[1:]):
        if m[i - 1] + x > 0:
            m[i] = m[i - 1] + x
            best_sum = max(m[i], best_sum)
        else:
            m[i] = 0
    return best_sum

infile = sys.argv[1]
file = open(infile, 'r')

for row in file:
    array = [int(i) for i in row.strip().split(',')]
    if (infile == "verify_2.txt"):
        del array[-1]

    print dynamic_programming(array)

# input_sizes = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
# methods = ['brute_force', 'divide_conquer', 'dynamic_programming']
# for method in methods:
#     for input_size in input_sizes:
#         numbers = [random.randint(-100, 100) for _ in xrange(input_size)]
#         start = time.time()
#         locals()[method](numbers)
#         end = time.time()
#         dt = end - start
#         print "%s,%i,%f" % (method, input_size, dt)
