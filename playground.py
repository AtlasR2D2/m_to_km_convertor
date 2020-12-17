def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(add(1,2,3,4,5))

def calculate(**kwargs):
    print(kwargs)

calculate(add=3, multiply=5)
