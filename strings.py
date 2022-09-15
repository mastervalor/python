def remove_blanks(string):
    new_string = ''
    for i in range(len(string)):
        if string[i] != ' ':
            new_string += string[i]
    return new_string

print(remove_blanks(" Pl ayTha tF u nkyM usi c "))

def nums_only(string):
    nums = ''
    for i in range(len(string)):
        try:
            if int(string[i]) >= 0:
                nums += string[i]
        except ValueError:
            continue
    return int(nums)

print(nums_only('0s1a3y5w7h9a2t4?6!8?0'))


def acronyms(string):
    acronym = ''
    if string[0] != ' ':
        acronym += string[0]
    for i in range(len(string)):
        if string[i] == ' ':
            acronym += string[i+1]
    return acronym.upper()


print(acronyms(" there's no free lunch - gotta pay yer way."))
print(acronyms("Live from New York, it's Saturday Night!"))


def arr_to_dic(arr1, arr2):
    dic = {}
    for i in range(len(arr1)):
        dic[arr1[i]] = arr2[i]
    return dic

print(arr_to_dic(["abc", 3, "yo"], [42, "wassup", True]))

def invertHash(assocArr):
    new_dic = {}
    for key,value in assocArr.items():
        new_dic[value] = key
    return new_dic

print(invertHash({"name": "Zaphod", "charm": "high", "morals": "dicey"}))