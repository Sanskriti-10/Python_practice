"""  Write a Python program to count how many times each character appears in a string using a dictionary.
(Example: "banana" → { 'b': 1, 'a': 3, 'n': 2 }) """

user_input=input("enter a word:")
dict={}

for i in range(len(user_input)):
  if user_input[i] in dict:
    dict[user_input[i]]+=1
  else:
    dict[user_input[i]]=1

print(dict) 
