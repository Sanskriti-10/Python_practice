#Write a Python program to find the second largest number in a list without using max() or sort().


user_input=list(map(int,input("enter list numbers:").split()))

if(len(user_input)<2):
  print("list should have atleast two numbers")

else:
  max=user_input[0]
  second_max=float('-inf')

  for i in range (1,len(user_input)):
   if user_input[i]>max:
    second_max=max
    max=user_input[i]
   elif user_input[i]>second_max and user_input[i]!= max:
     second_max=user_input[i]

  if second_max == float('-inf'):
     print("No second largest value (all elements might be same).")
  else:
    print("Second largest is:", second_max)
