import numpy as np

# sigmoid function
def nonlin(x, deriv=False):
    if deriv:
        return x * (1 - x)
    return 1 / (1 + np.exp(-x))

# input 
X = np.array([  [0,1,1],
                [1,1,1],
                [1,0,0],])
    
# output             
y = np.array([[0,1,1]]).T

# dropout
alpha, hidden_dim, dropout_percent, do_dropout = (0.5, 4, 0.2, True)

# seed random 
np.random.seed(1)

# weights initialization
syn0 = 2 * np.random.random((3, 4)) - 1

for iter in range(10000):

    # forward prop
    l0 = X
    l1 = nonlin(np.dot(l0, syn0))
    if do_dropout:
        l1 *= np.random.binomial([np.ones((len(X), hidden_dim))], 1 - dropout_percent)[0] * (1.0 / (1 - dropout_percent))

    # error
    l1_error = y - l1

    # back prop
    l1_delta = l1_error * nonlin(l1, True)
    syn0_delta = np.dot(l0.T, l1_delta)

    # weights update
    syn0 += syn0_delta

print("Trained output:")
print(l1)
