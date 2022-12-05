import re
# Loading and preprocessing data
with open('./2022/Day4/day4_input.txt', 'r') as f:
    lines = [list(map(int, re.split(',|-', g))) for g in f.readlines()]

# Challenge 1
count1 = sum([1 if (p11 <= p21 <= p22 <= p12) or (p21 <= p11 <= p12 <= p22) else 0 for p11, p12, p21, p22 in lines ])
print(count1)

# Challenge 2
count2 = sum([1 if p21 in range(p11, p12+1) or p11 in range(p21, p22+1) else 0 for p11, p12, p21, p22 in lines])
print(count2)