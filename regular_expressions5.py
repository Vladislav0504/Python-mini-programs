import sys
import re
pattern = r'\b(\w+)\1\b'
for line in sys.stdin:
  if re.search(pattern,line.rstrip()) != None:
  	print(line.rstrip())