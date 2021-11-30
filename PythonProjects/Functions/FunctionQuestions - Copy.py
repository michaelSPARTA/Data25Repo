print("\nQ1a\n")
# Q1a: Write a function which takes in an integer as an argument and returns the divisors of that number as a list
# e.g. f(12) = [1, 2, 3, 4, 6, 12]
# hint: range(1, n) returns a collection of the numbers from 1 to n-1

# A1a:


def divisors(integer: int):
    divisor_list = []
    for i in range(1, integer + 1):
        if integer % i == 0:
            divisor_list.append(i)
    return divisor_list


print(divisors(12))

print("\nQ1b\n")
# Q1b: Write a function which takes in two integers as arguments and returns true if one of the numbers
# is a factor of the other, false otherwise
# (bonus points if you call your previous function within this function

# A1b:


def factor(num1: int, num2: int):
    list1 = divisors(num1)
    list2 = divisors(num2)
    if num2 in list1 or num1 in list2:
        return True
    else:
        return False


print(factor(2, 4))
print(factor(2, 3))

# -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: write a function which takes a letter (as a string) as an input and outputs it's position in the alphabet
# alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
#             "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]

# A2a:


def alphabet_pos(letter: str):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]
    # for i in alphabet:
    #     if i == letter.lower():
    #         return alphabet.index(letter.lower())
    if letter.lower() in alphabet:
        return alphabet.index(letter.lower())
    else:
        return


print(alphabet_pos('a'))


print("\nQ2b\n")
# Q2b: create a function which takes a persons name as an input string and returns an
# ID number consisting of the positions of each letter in the name
# e.g. f("bob") = "1141" as "b" is in position 1 and "o" is in position 14

# A2b:


def name_id(name):
    # alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
    #             "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]
    id_number = ''
    for i in name:
        id_number = id_number + str(alphabet_pos(i))
    return id_number
    # for i in name:
    #     if i.lower() in alphabet:
    #         id_number = id_number + str(alphabet.index(i.lower()))
    #     else:
    #         return
    # return id_number


print(name_id('bob'))


print("\nQ2c\n")
# Q2c: Create a function which turns this ID into a password. The function should subtract
# the sum of the numbers in the id that was generated from the whole number of the id.
# e.g. f("bob") -> 1134 (because bob's id was 1141 and 1+1+4+1 = 7 so 1141 - 7 = 1134)

# A2c:


def password(name):
    summer = 0
    for i in name_id(name):
        summer = summer + int(i)
    return int(name_id(name)) - summer


print(password('bob'))


# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")
# Q3a: Write a function which takes an integer as an input, and returns true if the number is prime, false otherwise.

# A3a:


def is_prime():
    user_input = input('Please enter a number:  ')
    if user_input.isnumeric():
        if int(user_input) > 1:
            for i in range(2, int(user_input)):
                if int(user_input) % i == 0:
                    return False
            return True
        else:
            return False
    else:
        return 'That was not a number!'


print(is_prime())

print("\nQ3b\n")
# Q3b: Now add some functionality to the function which does not error if the user inputs something other than a digit

# A3b:


def is_prime():
    user_input = input('Please enter a number:  ')
    if user_input.isnumeric():
        if int(user_input) > 1:
            for i in range(2, int(user_input)):
                if int(user_input) % i == 0:
                    return False
            return True
        else:
            return False
    else:
        return 'That was not a number!'


print(is_prime())


# -------------------------------------------------------------------------------------- #






