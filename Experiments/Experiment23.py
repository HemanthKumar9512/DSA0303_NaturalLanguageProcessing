from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

text = [
    "I like Python programming.",
    "Python programming is easy.",
    "The weather is very hot."
]

v = TfidfVectorizer()
x = v.fit_transform(text)

score = cosine_similarity(x[0], x[1])[0][0]

print("Coherence score:", score)
