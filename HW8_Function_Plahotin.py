import random


def create_list(items, start, end):
    list_a = []  # Create 1st list
    i = 0
    while i < items:  # Insert random numbers in 1st list
        number_a = random.randint(start, end)
        list_a.append(number_a)
        i += 1
    return list_a


# Task 1

def list_sum(num_list):
    list_1 = sum(num_list)
    return list_1


print(list_sum(create_list(5, 0, 15)))


# Task 2

def list_min(num_list):
    list_2 = min(num_list)
    return list_2


print(list_min(create_list(15, 0, 50)))


# Task 3

def number_of_primes(num_list):
    amount = 0
    for i in num_list:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            amount += 1
    return amount


print(number_of_primes(create_list(15, 0, 50)))


# Task 4

def sum_of_del_symbol(del_symbol, num_list):
    summa = 0
    for i in num_list:
        if i == del_symbol:
            summa += 1
    return summa


print(sum_of_del_symbol(2, create_list(20, 0, 2)))

# Task 5

list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_2 = ['a', 'b', 'c', 'd', 'i', 'f', 'g']


def list_glue(list_1, list_2):
    result_list = []
    result_list.extend(list_1)
    result_list.extend(list_2)
    return result_list


print(list_glue(list_1, list_2))


# Task 6

def exponent(exp, num_list):
    exp_list = []
    for i in num_list:
        exp_list.append(i ** exp)
    return exp_list


print(exponent(2, create_list(10, 2, 9)))
