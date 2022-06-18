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

#write a function that given a list of buildings heights in a row ex. [1,4,2,3,5], return a list of visable building when viewed from the front. heights([1,4,2,3,5]) would return [1,4,5]

from ast import Import
import math


def heights(list):
    new_list = []
    x = 0
    for i in list:
        if i > x:
            new_list.append(i)
            x = i
    return new_list

print(heights([1,4,2,3,5]))

#write a function that given a number, returns whether or not that number has a whole intager square root. rootFinder(64) should return true while rootFinder(7) should return false 
def rootFinder(num):
    i = 1
    while i * i < num:
        i+=1
    if i * i == num:
        return True
    return False

#same but with built in
import math

def rootFinder(num):
    return int(math.sqrt(num))

print(rootFinder(64))
print(rootFinder(7))


# Write a function that given an amount of cents returns the fewest number of quarters, dimes, nickels, and pennies required to equal that amount.
#         coinCalculator(99) should return {"Quarters":3,"Dimes":2,"Nickels":0,"Pennies":4}
#     Bonus:
#         Account for Dollar increments as well (Ones/Fives/Tens/Twenties/Fifties/Hundreds)
#     Double Bonus:
#         Account for the elusive 2 dollar bills as well.

def coinCalculator(num):
    change = {
        "quarters" : 0,
        "dime" : 0,
        "nickles" : 0,
        "pennies" : 0,
    }
    dollars = {
        "hundreds": 0,
        "fifties": 0,
        "twenties": 0,
        "tens": 0,
        "fives": 0,
        "twos": 0,
        "ones": 0,
    }
    while num !=0:
        if num >= 25:
            change["quarters"] +=1
            num -= 25
        elif num >= 10:
            change["dime"] +=1
            num -= 10
        elif num >= 5:
            change["nickles"] +=1
            num -= 5
        else:
            change["pennies"] +=1
            num -=1
    while change["quarters"] < 3:
        if change["quarters"] >= 400:
            dollars["hundreds"] +=1
            change["quarters"] -= 400
        elif change["quarters"] >= 200:
            dollars["fifties"] += 1
            change["quarters"] -= 200
        elif change["quarters"] >= 80:
            dollars["twenties"] += 1
            change["quarters"] -= 80
        elif change["quarters"] >= 40:
            dollars["tens"] += 1
            change["quarters"] -= 40
        elif change["quarters"] >= 20:
            dollars["fives"] += 1
            change["quarters"] -= 20
        elif change["quarters"] >= 8:
            dollars["twos"] += 1
            change["quarters"] -= 8
        elif change["quarters"]>= 4:
            dollars["ones"] += 1
            change["quarters"] -=4

    return dollars, change

print(coinCalculator(99999999999))

# Threes and Fives
#         Write a function threesFives() that adds each value from 100 and 4000000 (inclusive) if that value is evenly divisible by 3 or 5 but not both.
#         display the final sum in the console

#     Sum to One Digit
#         Write a function sumToOne(num) that given a number sums that number's digits repeatedly until the sum is only one digit. return that final one digit results.
#         sumToOne(18) would return 9
#         sumToOne(923) would return 5

def threesFives():
    sum = 0 
    for i in range (100,4000001, 1):
        if (i % 3 == 0 or i % 5 == 0) and not i % 15 == 0:
            sum += i
    print(sum)

threesFives()


def sumToOne(num):
    num = str(num)
    for x in range(0,len(num)-1,1):
        if int(num[x]) + int(num[x+1]) < 10:
            return int(num[x]) + int(num[x+1])

print(sumToOne(917))

# create a function that given a string, returns the integer made from the string's digits. Given "0s1a3y5w7h9a2t4", 
# the function should return the number 1357924

def given_string(name):
    num = ""
    for i in range(len(name)):
        if (i % 2 ==0) & (i > 0):
            num += name[i]
    return num
print(given_string('0s1a3y5w7h9a2t4'))


def intExtraction(num):
    numbers = 0
    for i in range(len(num)):
        numbers = 

# create function clockHandAngles(seconds) that, given the number of seconds since 12:00:00,
# will print the angles ( in degress ) of the hour, minute and second hands. As a quick review, 
# there are 360 degrees in a full arc rotation. Treat "stright-up" 12:00:00 as 0 degress for all hands

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