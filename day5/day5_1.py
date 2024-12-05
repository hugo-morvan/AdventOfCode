import math
def all_increasing(idx):
    prev = -math.inf
    for e in idx:
        if e < prev : return False
        prev = e
    return True

my_set = []
dep = []
books = []

with open("input.txt", 'r') as text:
    lines = text.readlines()
    for line in lines:
        if len(line) == 1:continue
        if len(line) == 6: dep.append(line)
        else: books.append(line)

for line in dep:
    a,b = map(int ,line.split('|'))
    my_set.append(a)
    my_set.append(b)
       
uniques = list(set(my_set))
print(f"{uniques=}")


def build_dep(dep, book):
    dependencies = [0]*len(book)
    for line in dep:
        a,b = map(int ,line.split('|'))
        if a in book and b in book:
            col = book.index(b)
            dependencies[col] += 1
        else: continue
    print(f"{dependencies=}")
    return dependencies

correct_total = 0
incorrect_total = 0
for line in books:
    if len(line) != 6 and len(line) != 1:
        print(line)
        book = list(map(int ,line.split(',')))
        dependencies = build_dep(dep, book)
        #print(dep_order)
        if all_increasing(dependencies):
            mid = len(book)//2
            correct_total += book[mid]
        else:incorrect_total += book[dependencies.index(len(book)//2)]
    else: continue
print(correct_total)
print(incorrect_total)