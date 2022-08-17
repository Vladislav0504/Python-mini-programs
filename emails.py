from re import findall
from sys import stdin 
emails = r'\w+@\w+\.\w+'
print(*findall(emails, stdin.read()))