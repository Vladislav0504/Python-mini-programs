def percent(share, round_digits = 0):
  s = '.' + str(round_digits) + 'f'
  c = format(share * 100, s)
  if float(c) % 1 == 0:
  	return c + '%'
  else:
  	return str(float(c)) +'%'