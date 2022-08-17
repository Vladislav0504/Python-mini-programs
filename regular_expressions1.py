import sys
import re
pattern = r'cat'
for line in sys.stdin:
  if len(re.findall(pattern,line.rstrip())) >= 2:
  	print(line.rstrip())