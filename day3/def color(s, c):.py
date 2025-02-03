def color(s, c):
    return f'\x1b[{c}m{s}\x1b[0m'

for i in range(100):
    print(color(i,i))