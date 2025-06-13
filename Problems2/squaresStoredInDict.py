#6. Create a program that takes a number and returns a dictionary with keys from 1 to that number, and values as their squares.
#(Example: n = 3 → {1: 1, 2: 4, 3: 9})

user_input=int(input("enter the number:"))
squareDictionary={}
for i in range(1,user_input+1):
  squareDictionary[i]=i*i

print(squareDictionary)
