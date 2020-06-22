def combo_string(a, b):
  mn = min(a,b, key=len)
  mx = max(a,b, key=len)
  return mn + mx + mn
