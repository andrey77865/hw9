from decorators import processing_time


@processing_time
def some_func():
    print("Test")


some_func()
