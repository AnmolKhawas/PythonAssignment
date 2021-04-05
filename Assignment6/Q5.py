#Add 'ing' at the end where string length>=3
#if string ends with 'ing' then add 'ly'
#if string length<3,unchanged.

def add(str1):
    length=len(str1)
    if length>2:
        if str1[-3:]=='ing':
            str1 += 'ly'
        else:
            str1 += 'ing'
    return str1

print(add('ab'))
print(add('abc'))
print(add('string'))
        