#!/usr/bin/env python3

def print_fibonacci(length):
    starter = [0, 1]
    while len(starter) < length:
        new_number = starter[-1]+starter[-2]
        starter.append(new_number)
    print(starter)


print_fibonacci(9)

#     sequence = [0, 1]
#     while len(sequence) < length:
#         next_number = sequence[-1]+sequence[-2]
#         sequence.append(next_number)
#     print(sequence)


# print_fibonacci(9)
