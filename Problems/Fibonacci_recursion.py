#Write a Python function to compute the Fibonacci series up to n terms using recursion.


def fib(n):
  if n==0:
    return 0
  if n==1:
    return 1
  
  return fib(n-1)+fib(n-2)
  
def print_fib(n):
  for i in range(n):
   print(fib(i),end=' ')

number=int(input("enter the number of terms:"))
print("fibonacci series:")
print_fib(number)
