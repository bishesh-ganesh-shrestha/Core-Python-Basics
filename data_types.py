# str = "This is Bishesh Ganesh Shrestha"
# print(str[3:10])
# print(str[:10])
# print(type(str[:10]))
# print(str*2)

# type1 = type([1,2.0,'Bishesh'])
# print(type1)

# type2 = type((1,2.0,'Bishesh'))
# print(type2)

# type3 = type([(1,2,3), [4,5,6]])
# print(type3)

# list1 = [1, 'Bishesh', True, 100.128]
# print(list1[:2])

# tuple1 = (1, 'Bishesh', True, 100.128)
# print (tuple1[:2])

# list1[1] = 'Ganesh'
# print(list1)

# tuple1[1] = 'Ganesh'
# # print(tuple1)

# range1 = range(10)
# print(type(range1))

# for i in range(4):
#   print(i)

# for i in range(1,4):
#   print(i)

# for i in range(1,10,2):
#   print(i)
  
# b1 = bytes([72, 101, 108, 108, 111])  
# print(b1)
# b1[0] = 74

# b2 = bytearray([72, 101, 108, 108, 111])  
# print(b2)
# b2[0] = 74
# print(b2)
# print(b2 == bytearray(b'Jello'))

# mv1 = memoryview(b2)
# print(mv1)

# str = 'Hello'
# mv2 = memoryview(bytes(str, 'utf-8'))
# print(mv2)

# DICTIONARY
# d1 = {'name': 'Bishesh', 'age': 22}
# d2 = {
#   'name': 'Jack',
#   22: True
# }
# print(d1)
# print(d2)
# print(type(d1))
# print(type(d2))

# SET
# set1 = {1,2,'Bishesh'}
# print(type(set1))
# print(set1)

# NoneType
# a = None
# print(a)
# print(type(a))

# Type Conversion
print(int('100'))
print(type(str(11)))
print(tuple([1,2,3]))
print(list((1,2,3)))