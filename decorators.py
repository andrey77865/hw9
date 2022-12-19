def two_commands_func(func):
    def wrapper(*args):
        try:
            value = func(*args)
        except TypeError:
            print(f"Give me name and phone separated by space.")

    return wrapper


def one_command_func(func):
    def wrapper(*args):
        try:
            value = func(*args)
        except TypeError:
            print(f"Give me name or phone")

    return wrapper
