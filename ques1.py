# list = [1,5,6,8,9]

# print(list)
# list.append(5)
# print(list)
# list.remove(8)
# print(len(list))

import ctypes

class DynamicArray:
   def __init__(self):
      self.size = 1
      self.n = 0
      self.A = self.__make_array(self.size)

   def __len__(self):
      return self.n

   def __make_array(self,capacity):
      return (capacity*ctypes.py_object)()

L = DynamicArray()
len(L)

L = [10,20,30]
print(L)

L.append('hello')
print(L)