"""Write a Python program to remove duplicates from a list entered by the user while keeping the original order.
(Example: Input – [1, 2, 2, 3, 1] → Output – [1, 2, 3])

"""

"""solution: Use a set to track seen elements and iterate through the list, appending only unseen items to the result. This ensures duplicates are skipped while maintaining the original order with O(n) time and space complexity."""


def removeDuplicates(list):   
  tracker=set()
  new_list=[]
  for x in list:
    if x not in tracker:
      new_list.append(x)
      tracker.add(x)
  return new_list    


input_list= list(map(int,input("enter the numbers:").split()))
print("the input list is:",input_list)
new_list=removeDuplicates(input_list)
print("the new list with removed duplicates is:",new_list)
