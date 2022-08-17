import sys
import re
pattern = r'human'
for line in sys.stdin:
  line = re.sub(pattern, 'computer', line.rstrip())
  print(line)