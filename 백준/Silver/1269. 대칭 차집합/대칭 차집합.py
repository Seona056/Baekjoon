import sys
input = sys.stdin.read().splitlines()
 
a = set(input[1].split())
b = set(input[2].split())
 
print(len(a^b))