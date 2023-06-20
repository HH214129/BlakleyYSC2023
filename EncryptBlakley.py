import numpy as np
import random as rd
import array as arr

def encrypt_blackley(secret, prime, threshhold, number_of_shareholder):

  x = secret
  p = prime
  k = threshold
  n = number_of_shareholder

  vecto_X = list(x for i in range (k))
  vecto_X[0]=x
  x=np.array(x)
  print(x)

  for i in range(1,k):
    vecto_X[i]=(rd.randint(1,p))
  x=np.array(vecto_X)

  A = np.ones((n, k)).astype(int)
  for r in range(1, n):
    for c in range(1, k):
      A[r,c] = A[r,c-1] + A[r-1,c]
  y=np.dot(A,x)
  y=np.array(y)

  h = arr.array('i',[y[i] for i in range(n)])
  for i in range (n):
    h[i] = y[i]%p
  keys= [A[i].tolist()+ [h[i]] for i in range(n)]
  print(keys)
  return keys