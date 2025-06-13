#3. Write a Python program to flatten a nested list (one level only).
#(Example: [1, [2, 3], 4] → [1, 2, 3, 4])

import ast

nested_list = ast.literal_eval(input("Enter a list: "))

flattenedList=[]
for ele in nested_list:
  if type(ele)==list:
    flattenedList.extend(ele)
  else:
    flattenedList.append(ele) 

print(flattenedList)
