"""
Module that holds the calculator's general functions.
"""

# Imports
import math

# basic operations
def sum(a: float, b: float):
  '''
  Returns the sum of a and b

  ### Types
  * a: float
  * b: float
  * Return: float
  '''
  
  return a + b

def subtraction(a: float, b: float):
  '''
  Returns the difference between a and b.

  ### Types
  * a: float
  * b: float
  * Return: float
  '''

  return a - b

def multiplication(a: float, b: float):
  '''
  Returns a times b.

  ### Types
  * a: float
  * b: float
  * Return: float
  '''
  return a * b

def division(a: float, b: float):
  '''
  Returns a divides by b.
  If b is equal to zero, raises an ZeroDivisionError.

  ### Types
  * a: float
  * b: float
  * return: float
  ''' 
  if b == 0.:
    raise ZeroDivisionError()
  else:
    return a / b

# intermediate operations
def power(a: float, b: float):
  '''
  Return a to the power of b

  ### Types
  * a: float
  * b: float
  * Return: float
  '''
  return math.pow(a, b)

def log(a: float, b: float):
  '''
  Returns the logarithm of a of base b
  ### Rules
  * a > 0
  * b > 0

  *If not, returns a ValueError*

  ### Types
  * a: float
  * b: float
  * Return: float
  '''
  if a <= 0 or b <= 0:
    raise ValueError('math domain error')
  else:
    return math.log(a, b)
  
if __name__ == '__main__':
  # tests
  a = 8
  b = 2
  print(f'Sum: {a} + {b} =  {sum(a, b)}')
  print(f'Subtraction: {a} - {b} =  {subtraction(a, b)}')
  print(f'Multiplication: {a} x {b} =  {multiplication(a, b)}')
  try:
    print(f'Division: {a} / {b} =  {division(a, b)}')
  except ZeroDivisionError:
    print('Division by zero')
  print(f'Power: {a} ^ {b} =  {power(a, b)}')
  print(f'Power: log({a}) base {b} =  {log(a, b)}')
  pass