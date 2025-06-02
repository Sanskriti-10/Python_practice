#Write a Python function to check whether a given number is a prime number or not.

def isPrime(num):
  for x in range(2,int(num**0.5)+1):
    if num%x==0:
      return False
  return True 

user_input=int(input("enter a number:"))
if isPrime(user_input):
  print("the number is prime")
else:
  print("the number is not prime") 
