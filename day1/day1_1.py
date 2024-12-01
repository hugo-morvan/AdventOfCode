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
dif = sum(abs(l-r) for l, r in zip(left, right))
print(dif)
