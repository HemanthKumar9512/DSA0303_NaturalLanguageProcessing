import nltk
import string
nltk.download('punkt_tab')
nltk.download('stopwords')

# Lowercase
text = "This Is A Sample Text."
print("Lowercase: ",text.lower())

#Sentence Tokenization
from nltk.tokenize import sent_tokenize
print("Sentence Tokenization: ", sent_tokenize(text))

#Word Tokenization
from nltk.tokenize import word_tokenize
print("Word Tokenization: ", word_tokenize(text))

# Remove Punctuation from text
text=text.translate(str.maketrans ('', '', string.punctuation))
print("Removed Punctuations: ", text)

#Remove Stopwords
from nltk.corpus import stopwords
words=word_tokenize(text)
print([w for w in words if w.lower() not in stopwords.words('english')])

#Count Total Words in a document
words=word_tokenize(text)
print(len(words))

#Calculate Word Frequency
from collections import Counter
print(Counter(word_tokenize(text)))
