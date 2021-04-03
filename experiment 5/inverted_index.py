!pip install nltk
!pip install numpy
import numpy as np
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize

def remove_punctuation(data):
 symbols = ["!","#","$","%","&","(",")","*","+","-",".","/",":",";","<","=",">","?","@","[","]","^","_","`","{","|","}","~","\n",",",".","“"]
 for i in symbols:
  for words in data:
   if i == words:
    data.remove(words)
 return data
rhymes=["I’m a little teapot Short and stout Here is my handle Here is my spout. When I get all steamed up, Then I shout, Just tip me over and pour me out!",
        "Johnny Johnny! Yes, Papa? Eating sugar? No, Papa. Telling lies? No, Papa. Open your mouth Ha! Ha! Ha!",
        "Chubby cheeks, dimple chin Rosy lips, teeth within Curly hair, very fair Eyes are blue – lovely too. Teacher’s pet, is that you? Yes, Yes, Yes!"]

rhymes_listed=[]
for i in range(3):
 rhymes_listed.append(word_tokenize(rhymes[i]))
 remove_punctuation(rhymes_listed[i])

unique_elements=[]
for i in range(3):
 for word in rhymes_listed[i]:
  if word not in unique_elements:
   unique_elements.append(word)

index_dict={}

for word in unique_elements:
  temp_arr=[]
  for i in range(3):
   if word in rhymes_listed[i]:
     temp_arr.append("id"+str(i+1))
  index_dict[word]=temp_arr
  print(word+": ",end='')
  for i in range (len(index_dict[word])):
   print(index_dict[word][i],end=" ")
  print("\n")
for word in unique_elements:
 key_position=[]
 word_doc_arr=[]
 for i in range (len(index_dict[word])):
  word_doc_arr.append(int(index_dict[word][i].split('id')[1])-1)
 print(word+": ",end='')
 index_dict_counter=0

 for j in word_doc_arr:
  key_position.clear()
  counter=1
  term_counter=0
  print("<",end="")
  print(index_dict[word][index_dict_counter],end=', ')
  index_dict_counter= index_dict_counter+1
  
  for words in rhymes_listed[j]:
   if word==words:
    term_counter=term_counter+1
  print(term_counter,end=', ')
  for words in rhymes_listed[j]:
   if word==words:
    key_position.append(counter)
   counter=counter+1
  print(key_position, end='')
  print(">",end=" ")
 print("\n")
