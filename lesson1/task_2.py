numbers = [1, 2, '0', '300', -2.5, 'Dog', True, 0o1256]


def convert_to_int(list_numbers):
    list_num = []
    for i in range(len(list_numbers)):
        try:
            if isinstance(int(list_numbers[i]), int):
                list_num.append(int(list_numbers[i]))
        except ValueError as err:
            print("Unexpected type occur:", type(list_numbers[i]), err)

    return list_num


num = convert_to_int(numbers)  # Display all numbers in the list
for x in range(len(num)):
    print(num[x])


def max_and_min_number(list_numbers):
    print("Max number in the list is: ", max(list_numbers))
    print("Min number in the list is: ", min(list_numbers))


print(max_and_min_number(num))
