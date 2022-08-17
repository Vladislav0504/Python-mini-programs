def sum_numbers(filename):
    s = 0
    with open(filename, 'r') as f:
      for line in f:
      	s += int(line)
    return s