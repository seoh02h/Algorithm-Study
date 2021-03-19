import sys


N = int(sys.stdin.readline())
card_num = list(map(int, sys.stdin.readline().split()))

M = int(input())
target_list = list(map(int, sys.stdin.readline().split()))

dict = {}

for check_num in card_num:
    if (check_num in dict):
        dict[check_num] += 1
    else:
        dict[check_num] = 1

print(' '.join(str(dict[target]) if target in dict else '0' for target in target_list))