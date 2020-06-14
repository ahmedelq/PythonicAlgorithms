def string_match(a, b):
  two_splitter = lambda s: [s[i:i+2] for i in range(len(s) - 1)]
  return sum(1 for x,y in zip(two_splitter(a),two_splitter(b)) if x == y)