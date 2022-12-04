import math
with open('./2022/Day3/day3_input.txt', 'r') as f:
    lines = [g[:-1] for g in f.readlines()]

# Challenge 1
compartments = [set(f[:len(f)//2]) & set(f[-len(f)//2:]) for f in lines]
print(sum([ord(list(f)[0]) - (96 if ord(f.pop()) > 97 else 38) for f in compartments]))

# Challenge 2
prios = []
for i in range(0, len(lines), 3):
    badge = (set(lines[i]) & set(lines[i+1]) & set(lines[i+2])).pop()
    prios.append(ord(badge)- (96 if ord(badge) > 97 else 38))
print(sum(prios))
