#Write a Python program to check if two strings are anagrams of each other.
#(Example: "listen" and "silent")

def checkAnagram(string1,string2):
  if len(string1)!=len(string2):
    return False
  dict={}
  for char in string1:
    dict[char]= dict.get(char,0)+1

  for char in string2:
    if char not in dict or dict[char]==0:
      return False
    dict[char]-=1
  return True 

string1= input("enter first string:")
string2=input("enter second string:")

if checkAnagram(string1,string2):
  print("they are anagram")
else:
  print("not anagram")  
