import sys
import re
pattern = r"\\"
for line in sys.stdin:
  if re.search(pattern,line.rstrip()) != None:
  	print(line.rstrip())