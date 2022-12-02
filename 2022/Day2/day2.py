# Challenge 1
with open('./2022/Day2/day2_input.txt', 'r') as f:
    lines = f.readlines()


def get_score(f0, f1):
    win = 0
    if ord(f0) == ord(f1)-23:
        win = 3
    elif ((ord(f1) - ord(f0)) == 24) or (ord(f1) - ord(f0) == 21):
        win = 6

    return win + (ord(f1) - 87)

scores = [get_score(f[0], f[2]) for f in lines]
print(sum(scores))

# Challenge 2
def get_score2(f0, f1):
    if f1 == 'X':
        return (ord(f0)%3) + 1
    elif f1 == 'Y':
        return ord(f0) - 61
    else:
        if f0 == 'B':
            return 6 + 3
        else:
            return 6 + (2 if f0 == 'A' else 1)

scores = [get_score2(f[0], f[2]) for f in lines]
print(sum(scores))

