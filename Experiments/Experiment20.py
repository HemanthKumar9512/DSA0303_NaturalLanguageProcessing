from sklearn.feature_extraction.text import TfidfVectorizer

docs = [
    "I love Python",
    "Python is easy",
    "I love machine learning"
]

vectorizer = TfidfVectorizer()
matrix = vectorizer.fit_transform(docs)

print(matrix.toarray())
