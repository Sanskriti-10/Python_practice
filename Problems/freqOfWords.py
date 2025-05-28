""" Write a Python program that takes a sentence from the user and counts the frequency of each word.
(Example: "I love Python and I love coding" → Output: {'I': 2, 'love': 2, 'Python': 1, 'and': 1, 'coding': 1}) """


input_string=input("enter the sentence:").split()
list_of_words=list(input_string)
print(list_of_words)

dict={}

for x in list_of_words:
  if x in dict:
    dict[x]+=1
  else:
    dict[x]=1  


print(dict)
