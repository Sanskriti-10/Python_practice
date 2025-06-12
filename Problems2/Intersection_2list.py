#2. Write a function that returns the intersection of two lists (common elements only).
#(Example: [1, 2, 3] and [2, 3, 4] → [2, 3])

def merge(list1,list2):
  mergelist=[]
  set1=set(list1)

  for ele in list2:
    if ele in set1:
      mergelist.append(ele)
  return mergelist


list1=list(map(int,input("enter elements of list1:").split()))
list2=list(map(int,input("enter elements of list2:").split()))

print(merge(list1,list2))
