'''
Error calculation
'''
def relative_error(trueValue, value):
  '''
  Return the relative error given the true expected value and the
  value from method
  '''
  return abs(trueValue - value)/trueValue