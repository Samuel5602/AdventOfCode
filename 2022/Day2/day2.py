# a=x=rock, b=y=paper, c=z=scissors
# Challenge 1
with open('./2022/Day2/day2_input.txt', 'r') as f:
    lines = f.readlines()

# print(len(lines))

def get_score(f0, f1):
    # print(f'{f0}: {ord(f0)};    {f1}: {ord(f1)}')   
    win = 0
    if ord(f0) == ord(f1)-23:
        win = 3
    elif ((ord(f1) - ord(f0)) == 24) or (ord(f1) - ord(f0) == 21):
        win = 6

    return win + (ord(f1) - 87)


scores = [get_score(f[0], f[2]) for f in lines]
print(sum(scores))

'''
win:
A(65) Y(89) -> diff 24
B(66) Z(90) -> diff 24
C(67) X(88) -> diff 21

Lose:
A(65) Z(90) -> diff 25
B(66) X(88) -> diff 22
C(67) Y(89) -> diff 22
'''
