#1. Write a Python program to reverse the words in a sentence.
#(Example: "Python is fun" → "fun is Python")

input=input("enter the sentence:")
listOfWords=input.split()
reversed_list=listOfWords[::-1]
result=' '.join(reversed_list)
print(result)
