import sys
import re
pattern = r'\b(\w)(\w)(\w*)\b'
for line in sys.stdin:
  line = re.sub(pattern, r'\2\1\3', line.rstrip())
  print(line)