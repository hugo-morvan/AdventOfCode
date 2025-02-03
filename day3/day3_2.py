import re

pattern = r'mul\(\d{1,3},\d{1,3}\)'
do = r'do\(\)'
dont = r"don't\(\)"

res=0
RED= 31
GREEN = 32
def color(s, c):
    return f'\x1b[{c}m{s}\x1b[0m'
mode = True
with open("input.txt", 'r') as text:
    
    ops = []
    ops_idx = []
    dos = []
    donts = []

    lines = text.readlines()
    for line in lines:
        print("____________________________________________________________")
        #print(line)
        my_dict = {}
        found = re.finditer(pattern, line)
        for f_obj in found:
            idx = f_obj.span()[0]
            op = f_obj.group()
            my_dict[idx] = op
        print(my_dict)
        new_dos = re.finditer(do, line)
        idx_do = [d.span()[0] for d in new_dos]
        print(idx_do)

        new_donts = re.finditer(dont, line)
        idx_dont = [d.span()[0] for d in new_donts]
        print(idx_dont)

        instructions = {}
        for i in idx_do: instructions[i] = True
        for i in idx_dont: instructions[i] = False
        out = ""    
        print(instructions)
        
        for i in range(len(line)):
            if i in instructions.keys():
                mode = instructions[i]
            if mode:
                
                if i in my_dict.keys():
                    op = my_dict[i]
                    out += color(line[i], 35)
                    #print(f"adding {op} at index {i}")
                    numbers = re.findall(r'\d+', op)
                    a,b = map(int, numbers)
                    #print(a,b)
                    res += a*b
                else:
                    out += color(line[i], GREEN)
            else:
                out+= color(line[i], RED)
                if i in my_dict.keys():
                    op = my_dict[i]
                    #print(f"ignoring {op} at index {i}")
            
        print(out)

print(f"{res:_}")