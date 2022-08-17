import sys
import re
pattern = r'\b[Aa]+\b'
for line in sys.stdin:
  line = re.sub(pattern, 'argh', line.rstrip(),count = 1)
  print(line)