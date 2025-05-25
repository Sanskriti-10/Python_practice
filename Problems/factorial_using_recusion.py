"""Write a Python program using recursion to calculate the factorial of a number entered by the user.
(Example: factorial of 5 is 5 × 4 × 3 × 2 × 1 = 120)"""

def factorial(n):
  if n==0 or n==1:
    return 1 #base case
  
  return factorial(n-1)*n

user_input=int(input("enter a number:"))
print("factorial of entered number is",factorial(user_input))
