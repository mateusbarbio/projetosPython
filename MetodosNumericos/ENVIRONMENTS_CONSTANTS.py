'''
Environment constants
'''

# Functions
def epsilon():
  '''
  Return the machine precision.
  '''
  e = 1
  while True:
    e /= 2
    r = 1 - e
    if r == 1:
      break
  e *= 2
  return e

# Date and time formats
DATE_FORMAT = '%d/%m/%y'
TIME_FORMAT = '%H:%M'
FULL_TIME_FORMAT = '%d/%m/%y %H:%M'

# Methods constants
PRECISION = 1e-2

if __name__ == '__main__':
  pass