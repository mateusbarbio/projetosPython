'''
Functions to be studied
'''
# Imports


def func(x):
  '''
  f(x) = x^2 + 2
  '''
  return x**2 + 2

def func_diff(x):
  '''
  f'(x) = 2x
  '''
  return 2*x

def func_primitive(x):
  '''
  F(x) = (1/3)x^3 + 2x
  '''
  return (1/3)*x**3 + 2*x

def func_integration(x0, x1):
  '''
  integral[f(x)] from x0 to x1 = F(x1) - F(x0)
  '''
  return func_primitive(x1) - func_primitive(x0)