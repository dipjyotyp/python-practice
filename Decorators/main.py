def f1(func):
    def wrapper(*args, **kwargs):
        print("Started")
        val = func(*args, **kwargs)
        print("Ended")
        return val
    
    return wrapper

@f1
def f(a, b=3):
    print(a * b)

# print(f1(f))
# f1(f)()

# f = f1(f)
# f()

# x = f1(f)
# x()

# f("Hello, World! ")

@f1
def add(x,y):
    return x + y

print(add(1,2))