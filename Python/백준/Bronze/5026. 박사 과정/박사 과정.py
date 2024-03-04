import sys

N = int(input())

assignments = [sys.stdin.readline().strip() for i in range(N)]
answer = []

for assignment in assignments:

    if assignment == 'P=NP':
        answer.append('skipped')

    else:
        temp = assignment.split('+')
        result = int(temp[0]) + int(temp[-1])
        answer.append(result)
        

for i in range(N):
    print(answer[i])