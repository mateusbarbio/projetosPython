'''
Prompt functions
'''
# Imports
from datetime import datetime
from ENVIRONMENTS_CONSTANTS import *

def centralized_message(msg, totalLength, spaceChar = '-'):
  msg1 = msg
  msg1Length = len(msg)
  spaceLength = totalLength - msg1Length
  msg = f'{spaceChar*(spaceLength//2)}{msg1}{spaceChar*(totalLength - (msg1Length + spaceLength//2))}'
  return msg

def current_time(format = FULL_TIME_FORMAT):
  now = datetime.now()
  str = now.strftime(format)
  return str

def system_message(msg):
  print(f'[SYS - {current_time()}] : {msg}')

def init_application():
  msg = f'{'-'*10}[RODANDO A APLICAÇÃO]{'-'*10}'
  print(msg)
  t0 = datetime.now()
  return msg, t0

def end_application(totalLength):
  msg1 =  '[FIM DA APLICAÇÃO]'
  msg = centralized_message(msg1, totalLength)
  tf = datetime.now()
  print(msg)
  return msg, tf

def init_test(totalLength, description = ''):
  msg1 = f'[TESTE: {description.upper()}]' if description != '' else '[TESTE]'
  msg = centralized_message(msg1, totalLength, '*')
  print(msg)
  t0 = datetime.now()
  return msg, t0

def end_test(totalLength):
  msg1 = '[FIM DE TESTE]'
  msg = centralized_message(msg1, totalLength, '*')
  print(msg)
  tf = datetime.now()
  return msg, tf

def used_time(name, time):
  msg = f'{name.upper()} ::> {time.total_seconds()} s'
  system_message(msg)