import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"время выполнения: {end - start}")
        return result

    return wrapper


@timer
def fast_function():
    time.sleep(1)
    print("fast function done!")

@timer
def slow_function():
    time.sleep(3)
    print("slow function done!")


fast_function()
slow_function()