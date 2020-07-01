def alarm_clock(day, vacation):
  if (vacation):
    if not day % 6:
      return 'off'
    return '10:00'
  if not day % 6:
    return '10:00'
  return '7:00'
