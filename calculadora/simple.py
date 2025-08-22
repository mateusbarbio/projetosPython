'''
Simple calculator.
'''

# imports
import functions as fun

# Environment constants
WIDTH = 50
MAIN_LIMITER = '='
SECOND_LIMITER = '-'
TITLE = 'SIMPLE CALCULATOR'
VERSION = (1,0,0)

# Prompt configuration
# Lines
def mainLine(n: int):
  '''
  Draws a line with MAIN_LIMITER character n times

  ### Types
  * n: int
  * Return: string
  '''
  print(n*MAIN_LIMITER)

def secondLine(n: int):
  '''
  Draws a line with SECOND_LIMITER character n times.

  ### Types
  * n: int
  * Return: string
  '''
  print(n*SECOND_LIMITER)

# Decorators
def mainBlock(function):
  '''
  Decorator that wraps the functions's content within lines.
  '''
  def wrapper(*args, **kwargs):
    mainLine(WIDTH)
    result =  function(*args, *kwargs)
    mainLine(WIDTH)
    return result
  return wrapper

# prompts
def title(s):
  '''
  Prints the string in uppercase and centered

  ### Types
  * s: string
  '''
  l2 = len(s)
  l1 = (WIDTH - l2)//2
  l3 = WIDTH - l1 - l2
  sf = f'{l1*' '}{str.upper(s)}{l3*' '}'
  print(sf)

def mainTitle():
  '''
  Prints the calculator title and its versions in uppercase.
  '''
  s1 = f' VER.:{VERSION[0]:>2d}.{VERSION[1]:^1d}.{VERSION[2]:<2d}'
  # l1 + [l2] + l3 + [l4]
  l4 = len(s1)
  l1 = (WIDTH - len(TITLE))//2
  l3 = (WIDTH - l1 - len(TITLE)) - l4
  s2 = f'{l1*' '}{TITLE}{l3*' '}{s1}'
  print(s2)


if __name__ == '__main__':
  mainTitle()
  title('Mateus barbio')
  pass