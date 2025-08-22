'''
Error calculation
'''
def relative_error(trueValue, value):
  '''
  Return the relative error given the true expected value and the
  value from method
  '''
  if trueValue != 0.0:
    return abs(trueValue - value)/trueValue
  else:
    return abs(trueValue - value)