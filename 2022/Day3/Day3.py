import math
with open('./2022/Day3/day3_input.txt', 'r') as f:
    lines = [g[:-1] for g in f.readlines()]

# Challenge 1
compartments = [(set(f[:int(len(f)/2)]).intersection(set(f[-int(len(f)/2):])), ord(str(set(f[:int(len(f)/2)]).intersection(set(f[-int(len(f)/2):])).pop()))) for f in lines]

prios = [ord(f[0].pop()) - (96 if list(f)[1] > 97 else 38) for f in compartments]
print(sum(prios))