'''
Mathematical methods for differentiation.
'''
# Imports
from ENVIRONMENTS_CONSTANTS import *

# Functions
def BFD(fun, x0, e = PRECISION):
  '''
  Return the function's differentiation at x = x0 using the pass e
  using the Backward Finite Difference method.

  * fun: function
  * x0: float
  * e: float
  * return: float
  '''
  x1 = x0 - e
  y1 = fun(x1)
  y0 = fun(x0)
  r = (y0 - y1)/(x0 - x1)
  return r

def FFD(fun, x0, e = PRECISION):
  '''
  Return the function's differentiation at x = x0 using the pass e
  using the Forward Finite Difference method.

  * fun: function
  * x0: float
  * e: float
  * return: float
  '''
  x1 = x0 + e
  y1 = fun(x1)
  y0 = fun(x0)
  r = (y1 - y0)/(x1 - x0)
  return r

def CFD(fun, x0, e = PRECISION):
  '''
  Return the function's differentiation at x = x0 using the pass e
  using the Central Finite Difference method.

  * fun: function
  * x0: float
  * e: float
  * return: float
  '''
  x1 = x0 + e
  x0f = x0 - e
  y1 = fun(x1)
  y0 = fun(x0f)
  r = (y1 - y0)/(x1 - x0f)
  return r