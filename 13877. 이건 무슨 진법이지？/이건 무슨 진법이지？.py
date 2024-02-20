import sys
T = int(input())  
each_line_info = [sys.stdin.readline().strip() for i in range(T)] # a = ["1 23", "2 56"]

def to_8(x):
    if '8' in x or '9'in x:
        return 0
            
    else:
        result = [int(int(x[number])*8**(len(x)-1-number)) for number in range(len(x))]
        return sum(result)
       
def to_16(x):
    result = [int(int(x[number])*16**(len(x)-1-number)) for number in range(len(x))]
    return sum(result)

for i in each_line_info:
    
    K, numbers = i.split()
    
    print(int(K), int(to_8(numbers)), int(numbers), int(to_16(numbers)))



# 발생한 에러로 마지막 출력값의 형태가 str로 된 것들이 있어서 자꾸
# 에러가 발생했다... 문제를 잘읽자..
# 그리고 더하여 발생한 에러로 오타가 있었다...