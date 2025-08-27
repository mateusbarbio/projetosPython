'''
Mathematical methods for integration.
'''
# Imports
from ENVIRONMENTS_CONSTANTS import *
import numpy as np
import math

def simpson(fun, xi, xf, e = PRECISION):
  '''
  Return the integration of the function fun from xi to xf using the precision e
  for subsets range.

  * fun: function
  * xi: float
  * xf: float
  * e: float
  * return: float
  '''
  n = math.ceil((xf - xi)/e + 1)
  if n%2 == 0:
    n += 1

  x = np.linspace(xi, xf, num = n)
  dx = x[1] - x[0]
  
  r = 0.
  for i in range(0, n):
    xr = x[i]
    yr = fun(xr)
    if i == 0 or i == n:
      r += yr
    elif i%2 == 1:
      r += 4*yr
    else:
      r += 2*yr
  r *= (1/3)*dx

  return r