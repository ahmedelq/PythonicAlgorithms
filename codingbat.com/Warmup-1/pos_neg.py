def pos_neg(a, b, negative):
  is_a_pos = a > 0
  is_b_pos = b > 0 
  pos_neg  = (not is_a_pos and is_b_pos) or (is_a_pos and not is_b_pos)
  is_both_neg = not is_a_pos and not is_b_pos
  return (not negative and pos_neg) or (negative and is_both_neg)