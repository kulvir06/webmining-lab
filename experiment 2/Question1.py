!pip install nltk
import nltk
nltk.download('stopwords')
nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

f = open('demo.txt','r')
paragraph = f.read()

stop_words = set(stopwords.words('english'))

words_tokens = word_tokenize(paragraph)
filtered_paragraph = [w for w in words_tokens if not w in stop_words]

#alternate way to filter paragraph
# for w in words_tokens:
#   if w not in stop_words:
#     filtered_paragraph.append(w)
print(words_tokens)
print(filtered_paragraph)
