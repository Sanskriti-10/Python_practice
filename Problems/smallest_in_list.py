#Write a Python program to find the smallest number in a list entered by the user.

input_list=list(map(int,input("enter numbers:").split()))
print(input_list)

smallest=input_list[0]

for number in input_list:
  if number<smallest:
    smallest=number

print("smallest number in the list is:",smallest)
