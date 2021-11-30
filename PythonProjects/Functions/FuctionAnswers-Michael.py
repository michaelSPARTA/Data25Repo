# print("\nQ1a\n")
# # Q1a: Write a function which takes in an integer as an argument and returns the divisors of that number as a list
# # e.g. f(12) = [1, 2, 3, 4, 6, 12]
# # hint: range(1, n) returns a collection of the numbers from 1 to n-1
#
# # A1a:
#
#
# def divisors(num: int = 0):
#     list1 = []
#     for x in range(1, num + 1):
#         if num % x == 0:
#             list1.append(x)
#     return list1
#
#
# a = 8
# print(divisors(a))
#
#
# print("\nQ1b\n")
# # Q1b: Write a function which takes in two integers as arguments and returns true if one of the numbers
# # is a factor of the other, false otherwise
# # (bonus points if you call your previous function within this function
#
# # A1b:
#
#
# def factor(num1: int = 0, num2: int = 0):
#     if num1 % num2 == 0 or num2 % num1 == 0:
#         return True
#     else:
#         return False
#
#
# a = 2
# b = 2
# print(factor(a, b))
#
# # -------------------------------------------------------------------------------------- #
#
# print("\nQ2a\n")
# # Q2a: write a function which takes a letter (as a string) as an input and outputs it's position in the alphabet
# # alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
# #             "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]
#
# # A2a:
#
#
# def alphabet_pos(letter: str = 0):
#     alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
#                 "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
#     for x in alphabet:
#         if letter.lower() == x:
#             pos = alphabet.index(x)
#     return pos
#
#
# print(alphabet_pos('b'))
#
# print("\nQ2b\n")
# # Q2b: create a function which takes a persons name as an input string and returns an
# # ID number consisting of the positions of each letter in the name
# # e.g. f("bob") = "1141" as "b" is in position 1 and "o" is in position 14
#
# # A2b:
#
#
# def name_pos(name: str = 0):
#     pos = ''
#     for x in name:
#         pos += str(alphabet_pos(x))
#     return pos
#
#
# print(name_pos('aaa'))
#
# print("\nQ2c\n")
# # Q2c: Create a function which turns this ID into a password. The function should subtract
# # the sum of the numbers in the id that was generated from the whole number of the id.
# # e.g. f("bob") -> 1134 (because bob's id was 1141 and 1+1+4+1 = 7 so 1141 - 7 = 1134)
#
# # A2c:
#
#
# def password(name: str = 0):
#     num = 0
#     p_word = 0
#     for x in name_pos(name):
#         num += int(x)
#         p_word = int(name_pos(name)) - num
#     return password
#
#
# print(password('bob'))
#
# # -------------------------------------------------------------------------------------- #
#
# print("\nQ3a\n")
# # Q3a: Write a function which takes an integer as an input, and returns true if the number is prime, false otherwise.
#
# # A3a:
#
#
# def prime(num: int = 0):
#     if num > 1:
#         for i in range(2, num):
#             if (num % i) == 0:
#                 return False
#         return True
#     else:
#         return False
#
#
# print(prime(13))
# print(prime(12))
#
# print("\nQ3b\n")
# # Q3b: Now add some functionality to the function which does not error if the user inputs something other than a digit
#
# # A3b:
#
#
# def prime(num):
#     if num.isnumeric():
#         x = int(num)
#         if x > 1:
#             for i in range(2, x):
#                 if (x % i) == 0:
#                     return False
#             return True
#         else:
#             return False
#     else:
#         print(f"Sorry that's not a number.")
#
#
# user_input = input(f'Enter a number I will check if it is prime:  ')
# print(prime(user_input))
# # -------------------------------------------------------------------------------------- #


