# import
import numpy as np

# sigmoid function
def nonlin(x,deriv=False):
    if(deriv==True):
        return x*(1-x)
    return 1/(1+np.exp(-x))
    
# input 
X = np.array([  [0,1,1],
                [1,1,1],
                [1,0,0],])
    
# output             
y = np.array([[0,1,1]]).T

# seed random 
np.random.seed(1)

# weights initialization
syn0 = 2*np.random.random((3,1)) - 1

for iter in range(10000):

    # forward prop
    l0 = X
    l1 = nonlin(np.dot(l0,syn0))

    # error
    l1_error = y - l1

    # back prop
    l1_delta = l1_error * nonlin(l1,True)

    # weights update
    syn0 += np.dot(l0.T,l1_delta)

print ("Trained output:")
print (l1)
