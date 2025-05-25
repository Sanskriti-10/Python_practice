"""Write a Python program to check if a word entered by the user is a palindrome or not.
(A palindrome is a word that reads the same backward as forward, like "madam" or "level") """

def checkPalindrome(word):
  reverse_word=word[::-1]
  if reverse_word==word:
    print("It is palindrome.")
  else:
    print("It is not palindrome.")  


user_input=input("Enter a word:")
checkPalindrome(user_input)
  
