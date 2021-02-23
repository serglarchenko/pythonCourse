def sum_of_three_or_five(number_):
    temp = 0
    for i in range(number_):
        if (i % 3 == 0) or (i % 5 == 0):
            temp = temp + i
    return print(temp)


sum_of_three_or_five(100000000)
