import os

working_directory = os.getcwd()
print(working_directory)


def return_user_id():
    print(os.getpid())


return_user_id()
