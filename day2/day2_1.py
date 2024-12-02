import math

def all_increasing(list):
    prev = -math.inf
    for e in list:
        if e < prev : return False
        prev = e
    return True

def all_decreasing(list):
    prev = math.inf
    for e in list:
        if e > prev : return False
        prev = e
    return True

def adj_check(list):
    #Any two adjacent levels differ by at least one and at most three.
    for i in range(len(list)-1):
        dif = abs(list[i]-list[i+1])
        if dif > 3 or dif < 1 : return False
    return True

safe = 0
with open("input.txt", 'r') as text:
    lines = text.readlines()
    for line in lines:
        nums = list(map(int, line.split()))
        if adj_check(nums) and (all_decreasing(nums) or all_increasing(nums)): safe +=1

print(safe)