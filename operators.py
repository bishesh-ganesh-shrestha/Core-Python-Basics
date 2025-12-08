# MEMBERSHIP OPERATOR
str = 'Python'
a = 'p'
b = 'P'
print(a in str) #false
print(b in str) #true

c = 'thon'
d = 'thony'
print(c not in str) #false
print(d not in str) #true

# IDENTITY OPERATORS
str2 = 'Anaconda'
str3 = str
print(str is str2)
print(str is str3)
print(str is not str3)
print(str is not str2)

print(id(str))
print(id(str2))
print(id(str3))

# WALRUS OPERATOR (assignment expression operator)
list = [1,2,3,4,5]
while (n := len(list)) > 0:
    print(list.pop(), end = " ")
print("\n")

results = []
for x in range(10):
    if (y := x * x) > 20:
        results.append(y)
        
print(results)