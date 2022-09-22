def recursive_sigma(num):
    if num > 0:
        return num + recursive_sigma(num-1)
    return 0

def recursive_factorial(num):
    if num > 1:
        return num * recursive_factorial(num-1)
    return 1