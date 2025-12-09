# def greet(name: str = 'Johnny'):
#     print('Hello ' + name)
    
# greet('Alice')
# print(greet.__annotations__)

def math(a: 10, b: 20) -> int:
    print(a + b)
    
math(5, 15)
math('f','g')
print(math.__annotations__)