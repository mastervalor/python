# def given_string(name):
#     num = ""
#     for i in range(len(name)):
#         if (i % 2 ==0) & (i > 0):
#             num += name[i]
#     return num
# print(type(given_string('0s1a3y5w7h9a2t4')))
def clockHandAngles(seconds):
    hours = 0 
    minutes = 0
    second = 0
    while seconds > 0:
        if seconds > 3600:
            hours += 1
            seconds -= 3600
        elif seconds > 60:
            minutes += 1
            seconds -= 60
    return f"{hours} and {minutes}"

print(clockHandAngles(3660))