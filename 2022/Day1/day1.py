# Challenge 1
with open('./2022/Day1/day1_input.txt', 'r') as f:
    lines = f.read()

lines = lines.split('\n\n')

lines = [f.split() for f in lines]

for i in range(len(lines)):
    lines[i] = [int(f) for f in lines[i]]

max = max([sum(f) for f in lines])
print(max)

# Challenge 2
sum_list = sorted([sum(f) for f in lines], key=lambda t: -t)
print(sum(sum_list[:3]))
