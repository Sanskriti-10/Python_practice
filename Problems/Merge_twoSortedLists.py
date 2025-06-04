#Write a Python function to merge two sorted lists into a single sorted list.
#(Don’t use sort() after merging — merge them manually)


def merge_lists(list1,list2):
  if len(list1)==0:
    return list2
  elif len(list2)==0:
    return list1
  
  i=0
  j=0
  merge=[]

  while i<len(list1) and j<len(list2):
    if list1[i]<list2[j]:
      merge.append(list1[i])
      i+=1
    elif list1[i]>list2[j]:
      merge.append(list2[j])
      j+=1
    else:
      merge.append(list1[i]) 
      merge.append(list2[j])         #remove this line if doesnt want to include duplicates.
      i+=1
      j+=1
 
  if i!=len(list1):                  #  merged.extend(list1[i:])
    while i<len(list1):              # merged.extend(list2[j:])  [alternative to using while for appending]
     merge.append(list1[i])
     i+=1
  if j!=len(list2):
    while j<len(list2):
      merge.append(list2[j])
      j+=1    
  return merge

list1=list(map(int,input("enter list1 elements:").split()))
list2=list(map(int,input("enter list2 elements:").split()))

print("merged sorted list:",merge_lists(list1,list2))



