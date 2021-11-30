# print("\nQ1a\n")
# # Q1a: Print only the first 5 numbers in this list
# x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]
#
# # A1a:
# i = 0
# while i < 5:
#     print(x[i])
#     i += 1
#
#
# print("\nQ1b\n")
# # Q1b: Now print only the even numbers in this list (the elements that are themselves even)
# x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]
#
# # A1b:
# for num in x:
#     if num % 2 == 0:
#         print(num)
#
#
# print("\nQ1c\n")
# # Q1c: Now only print the even numbers up to the fifth element in the list (e.g. 2, 4, 34)
# x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]
#
# # A1c:
# i = 0
# while i < 5:
#     if x[i] % 2 == 0:
#         print(x[i])
#     i += 1
#
#
# # -------------------------------------------------------------------------------------- #
#
#
# print("\nQ2a\n")
# # Q2a: from the list of names, create another list that consists of only the first letters of each first name
# # e.g. ["Alan Turing", "Leonardo Fibonacci"] -> ["A", "L"]
# names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]
#
# # A2a:
# first_list = []
# for i in names:
#     first_list.append(i[0])
#
# print(first_list)
#
#
# print("\nQ2b\n")
# # Q2b: from the list of names, create another list that consists of only the index of the space in the string
# # HINT: use your_string.index("substring")
# names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]
#
# # A2b:
# space = ' '
# space_list = []
# for i in names:
#     if space in i:
#         space_list.append(i.index(space))
#
# print(space_list)
#
#
# print("\nQ2c\n")
# # Q2c: from the list of names, create another list that consists of the first and last initial of each individual
# names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]
#
# A2c:
# initials_list = []
# for i in names:
#     firstInitial = i[0]
#     secondInitial = i[i.index(' ') + 1]
#     initials_list.append(firstInitial+secondInitial)
#
# print(initials_list)
#
#
# # -------------------------------------------------------------------------------------- #
#
#
# print("\nQ3a\n")
# # Q3a: Here is a list of lists, print only the lists which have no duplicates
# # Hint: This can be easily done by using sets as a set does not contain duplicates
# list_of_lists = [[1,5,7,3,44,4,1],
#                  ["A", "B", "C"],
#                  ["Hi", "Hello", "Ciao", "By", "Goodbye", "Ciao"],
#                  ["one", "Two", "Three", "Four"]]
#
#
# # A3a:
# for i in list_of_lists:
#     if len(i) == len(set(i)):
#         print(i)
# 
# 
# # -------------------------------------------------------------------------------------- #
# 
# 
# print("\nQ4a\n")
# # Q4a: Using a while loop, ask the user to input a number greater than 100, if they enter anything else,
# # get them to enter again (and repeat until the conditions are satisfied). Finally print the number that
# # they entered
#
# # A4a:
# user_input = input('Please enter a number greater than 100:	 ')
# while int(user_input) <= 100:
#     user_input = input(f'{user_input} is not greater than 100, try again:  ')
#
# print(f'{user_input} is greater than 100')
#

# print("\nQ4b\n")
# # Q4b: Continue this code and print "prime" if the number is a prime number and "not prime" otherwise
#
# # A4b:
#
#
# def is_prime(num):
#     if num > 1:
#         for i in range(2, num):
#             if (num % i) == 0:
#                 return False
#         return True
#     else:
#         return False
#
#
# user_input = int(input('Please enter a number greater than 100:	 '))
# while user_input <= 100:
#     if is_prime(user_input):
#         print('prime')
#         user_input = int(input('That number was not greater than 100, try again:  '))
#     else:
#         print('not prime')
#         user_input = int(input('That number was not greater than 100, try again:  '))
#
# if is_prime(user_input):
#     print('prime')
# else:
#     print('not prime')
# print(f"Your number {user_input} is greater than 100")
