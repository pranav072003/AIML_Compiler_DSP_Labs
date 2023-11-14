import numpy as np

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def predict(sigma):
    for i in range(sigma.size):
        if sigma[i]>=0.5:
            sigma[i]=1
        else:
            sigma[i]=0
    sigma = np.array(list(map(int, sigma)))
    return sigma
    
def cost_function(X, y, theta):
    m = len(y)
    h = predict(sigmoid(X @ theta))
    for i in range(h.size):
        if h[i]==True:
            h[i]=1
        else:
            h[i]=0
    p = h[:, None]
    cost = 1/m * sum((p-y)**2)
    return cost

X_test = np.random.randn(50,100)
theta = np.zeros(X_test.shape[1])
predictions = predict(sigmoid(X_test @ theta))
y = np.random.randint(2,size=(X_test.shape[0],1))
error = cost_function(X_test, y, theta)
print('Predictions:- ',predictions)
print('Cost:- ', error)