def countdown(x):
    list = []
    for i in range(x,-1, -1):
        list.append(i)
    return list

print(countdown(5))

def pandr(x):
    print(x[0])
    return x[1]

print(pandr([1,2]))

def fplusl(x):
    return x[0] + len(x)

print(fplusl([1,2,3,4,5]))

def greaterthan(x):
    new = []
    if len(x)<2:
        return False
    for i in x:
        if i>x[1]:
            new.append(i)
    print(len(new))
    return new

print(greaterthan([5,2,3,2,1,4]))
print(greaterthan([1]))

def lengthvalue(size, value):
    new = []
    for i in range(0, size):
        new.append(value)
    return new

print(lengthvalue(4,7))
print(lengthvalue(6,2))