import math
with open('./2022/Day3/day3_input.txt', 'r') as f:
    lines = [g[:-1] for g in f.readlines()]

# Challenge 1
half_lens = [int(len(f)/2) for f in lines]

half_data = zip(lines, half_lens)

compartments = [set(f[:g]).intersection(set(f[-g:])) for f, g in half_data]

print(compartments[:5])

prios = [ord(list(f)[0]) - (96 if ord(list(f)[0]) < 65 else 38) for f in compartments]
print(len(prios))
# print(sum(prios))

# kleine letters (<27) - 96, grote letters (>26) -38