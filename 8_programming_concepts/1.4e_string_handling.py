# >> string handling
'''
>> including: length, substring, upper, lower
'''
# >> ----------------------------- << example code >>
def length(string):
    count = 0
    for i in string:
        count += 1
    return count

def substring(string, start, stop):
    substring = ''
    for char in range(start -1 , stop +1):
        substring += string[char]
    return substring

def upper(string):
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    upper = ''
    for i in string:
        if i.islower():
            upper += uppercase[lowercase.index(i)]
        else:
            upper += i
    return upper

def lower(string):
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    lower = ''
    for i in string:
        if i.isupper():
            lower += lowercase[uppercase.index(i)]
        else:
            lower += i
    return lower

print(length("string"))
print(substring("Andy was here!", 6, 8))
print(upper("Andy Bramwell"))
print(lower("Andy Bramwell"))