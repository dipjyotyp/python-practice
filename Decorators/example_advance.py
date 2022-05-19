import datetime


def log(func):
    def wrapper(*args, **kwargs):
        with open("log.txt", "a") as f:
            f.write("Called function with " + " ".join(
                [str(arg) for arg in args]) + " at " + str(datetime.datetime.now()) + "\n")
        val = func(*args, **kwargs)
        return val

    return wrapper


@log
def run(a, b, c):
    print(a+b+c)


run(1, 2, 90)
