# def call(x):
#     print(id(x))
#     x = x + 1
#     print(id(x))
    
# number = 10
# call(number)
# print(id(number))

# def greetings(name):
#     print (f"Hello, {name}!")
#     # return

# greetings('Bishesh')

# POSITIONAL ONLY
# def sum(a,b,/,c):
#     print (a+b+c)
    
# sum(2,3,c=5)

# KEYWORD ONLY
# def multiply(*,a,b,c):
#     print (a*b*c)
    
# multiply(a=2,c=3,b=4)

# ARBITRARY ARGUMENTS
# def sum(*args):
#     sum = 0
#     for i in args:
#         sum += i
#     return sum
    
# print(sum(2,3,4,5,6))

# ANONYMOUS FUNCTION
My_sum = lambda *args: sum(args)
print(My_sum(2,3,4,5))