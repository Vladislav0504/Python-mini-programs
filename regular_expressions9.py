import sys
import re
pattern = r'(\w)\1+'
for line in sys.stdin:
  line = re.sub(pattern, r'\1', line.rstrip())
  print(line)