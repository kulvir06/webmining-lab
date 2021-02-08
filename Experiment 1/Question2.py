#write a program to tokenize a sentence and multiple sentences

sentence = 'My name is Kulvir'
sentence = sentence.split()
print('tokenized sentence = ',sentence)

paragraph = {'My first name is Kulvir','My surname is Singh','I am 19 years old'}
text=[]
for sentence in paragraph:
  text.append(sentence.split())
print('tokenized paragraph : ',text)
 
