from re import findall
from sys import stdin 
pattern = r'-?\d*\.?\d+'
print(*findall(pattern, stdin.read()))