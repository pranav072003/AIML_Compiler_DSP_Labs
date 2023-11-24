# nueral network feedforward

import numpy as np

class NeuralNetwork:
    def __init__(self, input_dim, hidden_dims, output_dim):
      self.input_dim = input_dim
      self.hidden_dims = hidden_dims
      self.output_dim = output_dim
      self.weights = []
      self.biases = []
      self.activations = []
    
      # Initialize weights and biases
      if len(hidden_dims) == 0:
        self.weights.append(np.random.randn(input_dim, output_dim))
        self.biases.append(np.zeros((1, output_dim)))
        self.activations.append(np.zeros((1, output_dim)))
      else:
        self.weights.append(np.random.randn(input_dim, hidden_dims[0]))
        self.biases.append(np.zeros((1, hidden_dims[0])))
        self.activations.append(np.zeros((1, hidden_dims[0])))

        for i in range(1, len(hidden_dims)):
            self.weights.append(np.random.randn(hidden_dims[i-1], hidden_dims[i]))
            self.biases.append(np.zeros((1, hidden_dims[i])))
            self.activations.append(np.zeros((1, hidden_dims[i])))

        self.weights.append(np.random.randn(hidden_dims[-1], output_dim))
        self.biases.append(np.zeros((1, output_dim)))
        self.activations.append(np.zeros((1, output_dim)))

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def forward_propagation(self, X):
        self.activations[0] = self.sigmoid(np.dot(X, self.weights[0]) + self.biases[0])
        
        for i in range(1, len(self.hidden_dims) + 1):
            self.activations[i] = self.sigmoid(np.dot(self.activations[i-1], self.weights[i]) + self.biases[i])
        
        return self.activations[-1]

    def backward_propagation(self, X, y, learning_rate):
        m = X.shape[0]
        error = self.activations[-1] - y
        
        for i in range(len(self.hidden_dims), -1, -1):
            if i == len(self.hidden_dims):
                delta = error  *self.activations[i]*  (1 - self.activations[i])
            else:
                delta = np.dot(delta, self.weights[i+1].T)  *self.activations[i]*  (1 - self.activations[i])
            
            self.weights[i] -= learning_rate * np.dot(self.activations[i-1].T, delta) / m
            self.biases[i] -= learning_rate * np.mean(delta, axis=0)

    def train(self, X, y, epochs, learning_rate):
        for epoch in range(epochs):
            # Forward propagation
            outputs = self.forward_propagation(X)
            
            # Backward propagation
            self.backward_propagation(X, y, learning_rate)
            
            # Calculate loss
            loss = np.mean((outputs - y) ** 2)
            
            if epoch % 100 == 0:
                print(f"Epoch {epoch}: Loss = {loss:.4f}")

    def predict(self, X):
        return np.round(self.forward_propagation(X))

# Example usage
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])

# Initialize the neural network
nn = NeuralNetwork(input_dim=2, hidden_dims=[2], output_dim=1)

# Train the neural network
nn.train(X, y, epochs=1000, learning_rate=0.1)

# Make predictions
predictions = nn.predict(X)
print("Predictions:")
print(predictions)