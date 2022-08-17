import sys
import re
pattern = r'\b[01]+\b'
for line in sys.stdin:
  if len(re.findall(pattern, line.rstrip())) == 1:
  	for elem in re.findall(pattern, line.rstrip()):
  	  k, s = 0, 0
  	  for l in elem:
  	  	k += (-1)**s*(int(l))
  	  	s += 1
  	  if k % 3 == 0:
  	  	print(line.rstrip())
  	  	break