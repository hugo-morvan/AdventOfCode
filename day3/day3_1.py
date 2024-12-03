import re

pattern = r'mul\(\d{1,3},\d{1,3}\)'
ops = []

with open("input.txt", 'r') as text:
    lines = text.readlines()
    for line in lines:

        matches = re.findall(pattern, line)

        if matches: ops.extend(matches)
print(ops)
res = 0
for op in ops:
    numbers = re.findall(r'\d+', op)
    a,b = map(int, numbers)
    res += a*b
    
print(res)