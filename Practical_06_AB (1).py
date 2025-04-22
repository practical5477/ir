# Import necessary libraries
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Sample documents
documents = [
    "This is the first document.",
    "This document is the second document.",
    "And this is the third one.",
    "Is this the first document?",
    "The last document is here."
]

# Convert documents to TF-IDF matrix
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(documents)
# Apply K-means clustering
num_clusters = 2  # You can adjust the number of clusters as needed
n_init_value = 10  # You can adjust this value based on your needs

kmeans = KMeans(n_clusters=num_clusters, n_init='auto')
kmeans.fit(X)

# Get cluster labels
cluster_labels = kmeans.labels_

# Calculate silhouette score using the original documents and cluster labels
silhouette_avg = silhouette_score(X, cluster_labels)

# Print results
print("Cluster labels:", cluster_labels)
print("Silhouette Score:", silhouette_avg)
