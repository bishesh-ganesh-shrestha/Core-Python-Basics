# class Animal:
#     def __init__(self, name):
#         self.name = name
        
#     def sound(self):
#         print ("Animal Sound")
        
#     def setName(self, name):
#         self.name = name
        
#     def getName(self):
#         print (self.name)
    
# animal = Animal("Dog")
# animal.sound()
# animal.getName()
# animal.setName("Cat")
# animal.getName()

# class Dog(Animal):
#     def __init__(self, name, breed):
#         super().__init__(name)
#         self.breed = breed
        
#     def sound(self):
#         print("Bark")
        
#     def getBreed(self):
#         print(self.breed)
        
# dog = Dog("Buddy", "Golden Retriever")
# dog.sound()
# dog.getName()
# dog.getBreed()
# dog.setName("Max")
# dog.getName()

class Employee:
    def __init__(self):
        self
        
    def __del__(self):
        print(self.__class__.__name__, 'destroyed')
        
    def setName(self, name):
        self.name = name
        
    def getName(self):
        print(self.name)
        
emp = Employee()
# print(type(emp))
emp.setName("Holloway")
emp.getName()
emp.age = 22
print(emp.age)
del emp.age
# print(emp.age)
# print(emp.__class__.__name__)
emp2 = emp
emp3 = emp
print(id(emp), id(emp2), id(emp3))
del emp
# print(emp)
print(emp2)
print(emp3)
print(id(emp2), id(emp3))