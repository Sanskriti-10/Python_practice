#4. Implement a function that returns the frequency of each word in a paragraph (ignore punctuation).

import string

def freqWords(para):
  frequency={}
  for punct in string.punctuation:
    para = para.replace(punct, "")
  para = para.lower()
  para_to_list= para.split()

  for el in para_to_list:
    if el not in frequency:
      frequency[el]=1
    else:
      frequency[el]+=1  
  return frequency

para=input("enter a para:")

print(freqWords(para))
