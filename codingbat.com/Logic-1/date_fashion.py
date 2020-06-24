def date_fashion(you, date):
      high = (you > 8 or date > 8)
  return (high and you > 2 and date > 2) * 2 + (not high and (you > 2 and date > 2) )