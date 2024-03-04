import sys

n = int(input())

for _ in range(n):
    s = sys.stdin.readline().split('+')
    if 'P' in s[0]: 
        print('skipped')
    else:
        print(int(s[0])+int(s[1]))