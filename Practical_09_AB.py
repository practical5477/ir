from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import ndcg_score

# Generate synthetic labeled data (replace with your actual labeled data)
X, y = make_classification(n_samples=1000, n_features=10, n_classes=2, random_state=42)

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalize features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train RankSVM model
ranksvm_model = SVC(kernel='linear')
ranksvm_model.fit(X_train_scaled, y_train)

# Predict rankings on test set
y_pred = ranksvm_model.decision_function(X_test_scaled)

# Evaluate model effectiveness using NDCG (Normalized Discounted Cumulative Gain)
ndcg = ndcg_score(y_test.reshape(1, -1), y_pred.reshape(1, -1))
print("NDCG Score:", ndcg)
