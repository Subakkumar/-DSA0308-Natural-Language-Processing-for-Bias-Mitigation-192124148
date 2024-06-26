from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample corpus of documents
corpus = [
    "TF-IDF stands for Term Frequency-Inverse Document Frequency.",
    "It is a numerical statistic used to reflect the importance of a term in a document relative to a collection of documents.",
    "TF-IDF is often used in information retrieval and text mining.",
    "The higher the TF-IDF score of a term in a document, the more important it is to that document.",
    "The TF-IDF algorithm is based on the assumption that the importance of a term increases with its frequency in the document and decreases with the frequency in the corpus."
]

# Vectorize the documents using TF-IDF
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(corpus)

def retrieve_documents(query, corpus, tfidf_matrix, vectorizer, top_n=1):
    # Transform the query into TF-IDF representation
    query_tfidf = vectorizer.transform([query])
    
    # Calculate cosine similarity between the query and documents
    cosine_similarities = cosine_similarity(query_tfidf, tfidf_matrix).flatten()
    
    # Get the indices of top documents based on cosine similarity
    top_document_indices = cosine_similarities.argsort()[-top_n:][::-1]
    
    # Retrieve and return the top documents
    top_documents = [corpus[idx] for idx in top_document_indices]
    return top_documents

# Get input from the user
query = input("Enter your query: ")

# Retrieve top documents based on the query
top_documents = retrieve_documents(query, corpus, tfidf_matrix, vectorizer, top_n=2)

# Display the retrieved documents
print("Top Documents for the Query:")
for idx, document in enumerate(top_documents, start=1):
    print(f"Document {idx}: {document}")
