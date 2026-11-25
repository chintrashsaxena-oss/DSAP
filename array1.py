# #1 Initial code
# import array

# from array import *
# val = array('i', [1,2,3,4,5,6,7,8,9])

# for i in range(0,6):
#     print(val[i], end=" ")

# print('\n')

# for x in val:
#     print(x, end=" , ")

# print('\n')

#2 after some Changes

# from array import *

# val = array('i', [1,2,3,4,5,6,7,8,9])

# for i in range(0,len(val)):
#     print(val[i], end=" ")

# print('\n')

# for x in val:
#     print(x, end=" , ")

#3. check reverse order
# print('\n')
# val.reverse()
# for i in range(0,len(val)):
#     print(val[i], end=" , ")

# val.insert(1,40)
# val.append(60)

# copyArray = array(val.typecode, (x//2 for x in val))

# abc = val[::-1]
# # val.reverse()

# for i in range(0,len(val)):
#     print(val[i],end="  ")

# input from user

# from array import *
# from numpy import *
# arr = array('i', [])

# n = int(input("Enter a number"))

# for i in  range(0,n):
#     arr.append(int(input("Enter next input")))

# for x in arr:
#     print(x, end=" ")

# arr = array('i', [10,15,20,25,30])

# i = arr.index(15)
# print(i)

from array import *
from numpy import *

# val = array([1,2,4,5.2, "hey", "c"])
val = linspace(10,20,5)

for x in val:
    print(x, end=" ")