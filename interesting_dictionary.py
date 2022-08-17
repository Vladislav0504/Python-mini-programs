def dog_owners(pets):
  d = {}
  for el in pets:
    d[el[1:4]] = d.get(el[1:4],[]) + [el[0]]
  return d