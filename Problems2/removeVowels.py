#7. Write a function that removes all vowels from a given string and returns the result.
#(Example: "hello world" → "hll wrld")

def removeVowels(s):

   return ''.join([ch for ch in s if ch not in 'aeiouAEIOU'])

user_input= input("enter a sentence:")
print(removeVowels(user_input))
