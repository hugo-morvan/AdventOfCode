import math
def all_increasing(idx):
    prev = -math.inf
    for e in idx:
        if e < prev : return False
        prev = e
    return True

dep = []    # list of X|Y
books = []  # list of {a,b,c,...}

with open("input.txt", 'r') as text:
    lines = text.readlines()
    for line in lines:
        if len(line) == 1:continue
        if len(line) == 6: dep.append(line)
        else: books.append(line)


def build_dep(dep, book):
    """
    Given the dependency rules and a book ({a,b,c,...})
    returns a list containing the number of times a page in a book is dependent on another page
    Example: 
    dep = C|A, C|B, B|A and book = {A,B,C}
    returns [2,1,0]
    """
    dependencies = [0]*len(book)
    for line in dep:
        a,b = map(int ,line.split('|'))
        if a in book and b in book:
            col = book.index(b)
            dependencies[col] += 1
        else: continue
    #print(f"{dependencies=}")
    return dependencies

correct_total = 0   # part 1
incorrect_total = 0 # part 2

for line in books:
    if len(line) != 6 and len(line) != 1:
        book = list(map(int ,line.split(',')))
        dependencies = build_dep(dep, book)
        #print(dep_order)
        if all_increasing(dependencies):
            mid = len(book)//2
            correct_total += book[mid]
        else:
            incorrect_total += book[dependencies.index(len(book)//2)]
    else: continue
print(f"part 1: {correct_total}")
print(f"part 2: {incorrect_total}")