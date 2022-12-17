import time


def processing_time(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        value = func(*args, **kwargs)
        stop = time.perf_counter()
        result_time = stop - start
        print("Time: ", result_time)

        return value

    return wrapper


def trace(func):
    def wrapper(*args):
        try:
            value = func(*args)
        except TypeError:
            print(f"Give me name and phone separated by space")
            exit()
        except IndexError as error:
            print(
                f"Give me name and phone separated by space. You entered: {args}")
            exit()
        return value

    return wrapper
