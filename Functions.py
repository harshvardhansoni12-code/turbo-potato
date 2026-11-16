def hello(args):
    print("Hello, " + args + "!")

hello("harish")


# return keyword is used to return a value from a function. When a function is called, it can perform some operations and then return a value to the caller using the return statement. The returned value can be assigned to a variable or used directly in expressions.

def cube(num):
    return pow(num,3) # without return keyword print gives None

print(cube(4))