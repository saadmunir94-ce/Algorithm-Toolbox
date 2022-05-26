
def max_pairwise():
    n = input()
    nos = list(map(int, input().split()))
    nos = sorted(nos)
    print(nos[-2] * nos[-1])
max_pairwise()