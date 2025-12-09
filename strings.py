# str1 = 'Hello'
# str2 = 'World'
# print(str1 + str2)
# print('a' in str1)

# print("My name is %s" % (str1))
# print(str1.isdecimal())

# num = '1'
# print(num.isdecimal())

# str = 'HelloWorld'
# print(str.join(['My ', ' from ', ' Python']))

# print(max(str))
# print(min(str))

# VOWEL COUNT
str = input("Enter a string:")
count = 0
for x in str:
    if x.lower() in 'aeiou':
        count += 1
    
print("Number of vowels:", count)