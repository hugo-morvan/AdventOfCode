left = []
right = []
with open("1_1input.txt", 'r') as text:
    lines = text.readlines()
    for line in lines:
        l , r = map(int, line.split())
        left.append(l)
        right.append(r)
left.sort()
right.sort()
sim = sum(l*right.count(l) for l in left)
print(sim)
