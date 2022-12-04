import math
with open('./2022/Day3/day3_input.txt', 'r') as f:
    lines = [g[:-1] for g in f.readlines()]

# Challenge 1
compartments = [set(f[:int(len(f)/2)]).intersection(set(f[-int(len(f)/2):])) for f in lines]

prios = [ord(list(f)[0]) - (96 if ord(f.pop()) > 97 else 38) for f in compartments]
print(sum(prios))