def state_change(stateD):
  print('StateD:', stateD)
  if stateD > 15:
    stateD = 15
    print('DOWN to ', stateD)
  if stateD < 0:
    stateD = 0
    print('UP to ', stateD)
  b = stateD  + 16 
  print('b =',b)
  binD = bin(b)
  print(binD)


print(state_change(-6))