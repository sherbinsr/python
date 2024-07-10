from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample documents
documents = [
    "This is the first document.",
    "This document is the second document.",
    "And this is the third one.",
    "Is this the first document?"
]

# Create a CountVectorizer to convert text data into a bag-of-words representation
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(documents)

# Calculate cosine similarity
cosine_similarities = cosine_similarity(X, X)

# Print the similarity matrix
print("Cosine Similarity Matrix:")
print(cosine_similarities)

# You can access individual similarity scores like this:
# For example, similarity between document 0 and document 1
similarity_0_1 = cosine_similarities[0, 1]
print(f"Similarity between document 0 and document 1: {similarity_0_1}")
