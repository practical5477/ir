import math
from collections import Counter

def tokenize(text):
    # Simple tokenization, you might want to improve it based on your specific needs
    return text.lower().split()

def compute_tf(doc):
    # Computes term frequency (TF) for each term in the document
    word_count = Counter(tokenize(doc))
    total_words = len(tokenize(doc))
    tf = {word: count/total_words for word, count in word_count.items()}
    return tf

def compute_idf(documents):
    # Computes inverse document frequency (IDF) for each term in the collection of documents
    N = len(documents)
    idf = {}
    
    for doc in documents:
        terms = set(tokenize(doc))
        for term in terms:
            idf[term] = idf.get(term, 0) + 1
    
    idf = {term: math.log(N/frequency) for term, frequency in idf.items()}
    return idf

def compute_tf_idf(tf, idf):
    # Computes TF-IDF for each term in the document
    tf_idf = {term: tf[term] * idf.get(term, 0) for term in tf}
    return tf_idf

def compute_cosine_similarity(query_tf_idf, doc_tf_idf):
    # Computes cosine similarity between query and document TF-IDF vectors
    common_terms = set(query_tf_idf.keys()) & set(doc_tf_idf.keys())
    
    dot_product = sum(query_tf_idf[term] * doc_tf_idf[term] for term in common_terms)
    query_norm = math.sqrt(sum(value**2 for value in query_tf_idf.values()))
    doc_norm = math.sqrt(sum(value**2 for value in doc_tf_idf.values()))
    
    if query_norm == 0 or doc_norm == 0:
        return 0
    
    similarity = dot_product / (query_norm * doc_norm)
    return similarity

    
    similarity = dot_product / (query_norm * doc_norm)
    return similarity

def vector_space_model(documents, query):
    # Build TF-IDF vectors for documents and query
    tf_idf_vectors = []
    
    for doc in documents:
        tf = compute_tf(doc)
        idf = compute_idf(documents)
        tf_idf = compute_tf_idf(tf, idf)
        tf_idf_vectors.append(tf_idf)
    
    query_tf = compute_tf(query)
    query_idf = compute_idf(documents)
    query_tf_idf = compute_tf_idf(query_tf, query_idf)
    
    # Compute cosine similarity between query and each document
    similarities = []
    for doc_tf_idf in tf_idf_vectors:
        similarity = compute_cosine_similarity(query_tf_idf, doc_tf_idf)
        similarities.append(similarity)
    
    return similarities

# Example usage:
documents = [
    "This is the first document.",
    "This document is the second document.",
    "And this is the third one.",
    "Is this the first document?",
]

query = "This is a query document."

similarities = vector_space_model(documents, query)
print("Cosine Similarities:")
for i, sim in enumerate(similarities):
    print(f"Document {i + 1}: {sim}")
