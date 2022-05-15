# Write a function that accepts a list and returns whether that List has an even amount of values or an odd amount of values. oddOrEvenList([1,2,3]) should return odd while  oddOrEvenList([1,2,3,4]) will return even

def oddOrEvenList(list):
    if len(list)%2 ==0:
        return "even"
    return "odd"

print(oddOrEvenList([1,2,3,4]))

# write a function that given a string date such as "05/12/2022", return whether or not a person's birthday has passed this year. Birthday("07/29/1993") should return false
# bonus - return a string with the users current age and whether or not they have had a birthday, Birthday("07/29/1993") 
# should return "User is currently 28 years old and has not yet had their birthday this year"

def birthday(day):
    age =  2022 - int(day[6:])
    if int(day[0:2]) < 5:
        return f"User is currently {age} years old and have had their birthday this year"
    elif int(day[0:2]) == 5 and int(day[3:5])<=12:
        return f"User is currently {age} years old and have had their birthday this year"
    else:
        return f"User is currently {age} years old and has not yet had their birthday this year" 

print(birthday("07/29/1993"))

# given a string, detect whether or not it is in pangram ( contains all letters of the alphabet.) return True if it is False if not. ignore numbers and punctuation.
#     Panagram("the quick brown fox jumped over the lazy dog") should return true.

def minimum(input):
    min = input[0]
    for i in range(len(input)):
        if input[i] < min:
            min = input[i]
    return min

def maximum(input):
    max = input[0]
    for i in range(len(input)):
        if input[i] > max:
            max = input[i]
    return max

def average(input):
    sum = 0
    for i in range(len(input)):
        sum += input[i]
    return sum / len(input)

def minMaxAvg(input):
    min = minimum(input)
    max = maximum(input)
    avg = average(input)
    return [min, max, avg]

print(minMaxAvg([1,2,3,4]))