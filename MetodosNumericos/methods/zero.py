'''
Mathematical methods for function zero determination.
'''
# Imports
from ENVIRONMENTS_CONSTANTS import *

def bisection(fun, range, e = PRECISION):
  '''
  Bisection method for determination of function root given
  the range of search and the precision e.

  * fun: function
  * range: enumerable
  * e: float
  * return: float
  '''

  n = 1
  if len(range) != 2:
    raise ValueError('range must have two values') 
  x0 = range[0]
  x1 = range(1)
  y0 = fun(x0)
  y1 = fun(x1)
  r = []

  while True:
    xr = (x0 + x1)/2
    yr = fun(xr)

    # Continuação....  