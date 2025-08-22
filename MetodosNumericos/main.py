'''
Treino de cálculo numérico
'''
# Imports
from functions import *
import prompt as prt
from methods import differentiation as diff
from methods.error import relative_error

# main routine
if __name__ == '__main__':
  initialization = prt.init_application()
  msgLength = len(initialization[0])

  # TRUE VALUE - START
  test_start = prt.init_test(msgLength, 'valor real')[1]

  x0 = 0.
  x1 = 2.
  prt.system_message(f'f({x0}) = {func(x0)}, f({x1}) = {func(x1)}')
  prt.system_message(f"f'({x0}) = {func_diff(x0)}, f'({x1}) = {func_diff(x1)}")
  prt.system_message(f'Integral de f(x) de {x0} a {x1} = {func_integration(x0, x1): 1.2f}')

  test_end = prt.end_test(msgLength)[1]

  prt.used_time('test', test_end - test_start)
  # TRUE VALUE - END
  # BFD - START
  test_start = prt.init_test(msgLength, 'bfd')
  f0 = diff.BFD(func, x0)
  truef0 = func_diff(x0)
  err0 = relative_error(truef0, f0)

  f1 = diff.BFD(func, x1)
  truef1 = func_diff(x1)
  err1 = relative_error(truef1, f1)

  prt.system_message(f"f'({x0}) = {f0} ({err0*100: 1.2f}%), f'(x1) = {f1} ({err1*100: 1.2f}%)")

  test_end = prt.end_test(msgLength)
  # BFD - END

  # FFD - START
  test_start = prt.init_test(msgLength, 'ffd')
  f0 = diff.FFD(func, x0)
  truef0 = func_diff(x0)
  err0 = relative_error(truef0, f0)

  f1 = diff.FFD(func, x1)
  truef1 = func_diff(x1)
  err1 = relative_error(truef1, f1)

  prt.system_message(f"f'({x0}) = {f0} ({err0*100: 1.2f}%), f'(x1) = {f1} ({err1*100: 1.2f}%)")

  test_end = prt.end_test(msgLength)
  # FFD - END

  # CFD - START
  test_start = prt.init_test(msgLength, 'CFD')
  f0 = diff.CFD(func, x0)
  truef0 = func_diff(x0)
  err0 = relative_error(truef0, f0)

  f1 = diff.CFD(func, x1)
  truef1 = func_diff(x1)
  err1 = relative_error(truef1, f1)

  prt.system_message(f"f'({x0}) = {f0} ({err0*100: 1.2f}%), f'(x1) = {f1} ({err1*100: 1.2f}%)")
  test_end = prt.end_test(msgLength)
  # CFD - END

  finalization = prt.end_application(msgLength)