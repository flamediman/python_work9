
def func(a, b):
    if b == 0:
        return a
    else:
        return func(b, a % b)
print(func(4, 2))
