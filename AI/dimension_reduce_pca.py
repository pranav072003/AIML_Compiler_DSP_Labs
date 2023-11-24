# Dimension reduction using PCA 

import numpy as np

def preprocess_data(X):
    # Perform any necessary preprocessing steps, such as scaling or normalization
    # You can customize this function based on your specific dataset
    X = X.astype(float)

    # Subtract the mean from each feature
    X -= np.mean(X, axis=0)
    
    return X

def calculate_covariance_matrix(X):
    # Calculate the covariance matrix of the dataset
    covariance_matrix = np.cov(X.T)
    
    return covariance_matrix

def calculate_eigenvectors(covariance_matrix):
    # Calculate the eigenvectors and eigenvalues of the covariance matrix
    eigenvalues, eigenvectors = np.linalg.eig(covariance_matrix)
    
    # Sort the eigenvectors based on the eigenvalues in descending order
    sorted_indices = np.argsort(eigenvalues)[::-1]
    sorted_eigenvectors = eigenvectors[:, sorted_indices]
    
    return sorted_eigenvectors

def reduce_dimensions(X, eigenvectors, k):
    # Project the original data onto the selected principal components
    reduced_X = np.dot(X, eigenvectors[:, :k])
    
    return reduced_X

# Example usage
X = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Preprocess the data
X = preprocess_data(X)

# Calculate the covariance matrix
covariance_matrix = calculate_covariance_matrix(X)

# Calculate the eigenvectors
eigenvectors = calculate_eigenvectors(covariance_matrix)

# Reduce the dimensions
k = 2  # Number of principal components to keep
reduced_X = reduce_dimensions(X, eigenvectors, k)

print("Original Data:")
print(X)
print("Reduced Data:")
print(reduced_X)