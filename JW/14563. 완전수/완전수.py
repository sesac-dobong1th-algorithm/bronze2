import sys

def judge_perfect (a):
    divisor_list = []
    for i in range(1,a//2+1):
        if a%i == 0:
            divisor_list.append(i)
    
    if sum(divisor_list) >a:
        print("Abundant")
    elif sum(divisor_list) == a:
        print("Perfect")
    else:
        print("Deficient")

n = int(sys.stdin.readline())

test = sys.stdin.readline().split()

for j in range(n):
    judge_perfect(int(test[j]))