with open('./2022/Day1/day1_input.txt', 'r') as f:
    lines = f.read()

lines = lines.split('\n\n')

lines = [f.split() for f in lines]
for i in range(len(lines)):
    lines[i] = [int(f) for f in lines[i]]

print(lines[0])


