var_three = "Fizz"
var_five = "Buzz"
for x in range(1, 101):

    if x % 3 == 0 and x % 5 == 0:
        print(str(x) + var_three + var_five)

    elif x % 3 == 0 and x % 5 != 0:
        print(str(x) + var_three)

    elif x % 5 == 0 and x % 3 != 0:
        print(str(x) + var_five)

    else:
        print(x)
