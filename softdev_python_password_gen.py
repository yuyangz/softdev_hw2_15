#Yuyang Zhang
#SoftDev2 pd07
#K15 -- Do You Even List?
#2018-04-25

#created categories
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_case =  upper_case.lower()
#number = [x for x in range(10)]
number = "0123456789"
symbols = ".?!&#,;:_-*"

#checks if password is complete
#creates list for each type of character
#if each list has a value, then the password is valid
def check_valid(pw):
    upper =[1 for x in pw if x in upper_case]
    lower = [1 for x in pw if x in lower_case]
    num = [1 for x in pw if x in number]

    if len(upper) and len(lower) and len(num) > 0:
        return True
    else:
        return False

print check_valid("Ab1*")
print check_valid ("aaaa")
print check_valid("_____")
#checks strength
#each group of characters has a different value
#if the sum of values passes a certain point, it will reach a certain strength level
def check_strength(pw):
    upper =[1 for x in pw if x in upper_case]
    lower = [1 for x in pw if x in lower_case]
    num = [1 for x in pw if x in number]
    sym = [1 for x in pw if x in symbols]

    sum = 0
    for x in upper:
        sum += 1
    for x in lower:
        sum += 1
    for x in num:
        sum += 3
    for x in sym:
        sum += 5

    strength = sum/10
    if strength > 10:
        strength = 10
    return strength

print check_strength("aB4*")
print check_strength("aaaaBBBB4*bCDUJeffjuj")
print check_strength("aaaaBBBB4*bCDUJeffjuj***1232131")
print check_strength("aaaaBBBB4*bCDUJeffjuj**!!2021391039109")
print check_strength("aaaaBBBB4*bCDUJeffjuj**!!202139#!:-1039109")
