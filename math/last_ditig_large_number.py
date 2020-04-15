def last_digit(n, exp):
  if not exp: return 1
  di = {
      0:[0],
      1:[1],
      2:[2,4,8,6],
      3:[3,9,7,1],
      4:[4,6],
      5:[5],
      6:[6],
      7:[7,9,3,1],
      8:[8,4,2,6],
      9:[9,1]
  }
  ld = n % 10
  return di[ld] [ (exp % len(di[ ld ])) - 1 ]
