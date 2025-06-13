#5. Write a Python function that takes a list and returns a new list with elements in reverse order, without using reverse() or slicing.

def reverseList(inputList):
  reversedList=[]

  for i in range(len(inputList)-1,-1,-1):
    reversedList.append(inputList[i])

  return reversedList


inputList= list(map(int,input("enter elements of list:").split()))
print(reverseList(inputList))
