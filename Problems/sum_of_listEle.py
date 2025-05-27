#Write a Python program that takes a list of numbers and prints the sum of all the elements in the list.

def sumOfElements(list):
  sum=0
  for el in list:
    sum=sum+el
  return sum  


input_list=list(map(int,input("enter numbers:").split()))
print(input_list)

print("the sum of Numbers of the list is:",sumOfElements(input_list))
