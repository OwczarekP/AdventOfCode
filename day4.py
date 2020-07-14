def first_check(password_list):
    possibilities_1 = []
    for number in password_list:
        if len(str(number)) == 6:
            possibilities_1.append(number)
    return possibilities_1


def second_check(password_list):
    possibilities_2 = []
    for number in password_list:
        if  str(number) == "".join(sorted(str(number))):
            possibilities_2.append(number)
    return possibilities_2


def third_check(password_list):
    possibilities_3 = []
    for password in password_list:
        same_digit = 0
        for i in range(1, len(str(password-1))):
            if str(password)[i-1] == str(password)[i]: same_digit += 1
        if same_digit > 0: possibilities_3.append(password)
    return possibilities_3

def third_check_p2(password_list):
    possibilities_3 = []
    for password in password_list:
        number = str(password)
        for digit in number:
            count_nb = number.count(digit)
            if count_nb == 2:
                possibilities_3.append(password)               
                break  
    return possibilities_3


def possibilities_check(password_list):
    first = first_check(password_list)
    second = second_check(first)
    third = third_check(second)
    return len(third)

def possibilities_check_p2(password_list):
    first = first_check(password_list)
    second = second_check(first)
    third = third_check_p2(second)
    return len(third)


input = list(range(372037, 905157))
print(possibilities_check(input))
print(possibilities_check_p2(input))