numbers = []
while True:
    S = int(input())
    if S == 0:
        break
    numbers.append(S)

numdict = {}

for number in numbers:

    ans = [] # numdict이라는 dictionary에 해당 number라는 key의
                #value로 넣을 수레, 그렇기에 매번 초기화 시켜줘야한다.

    xnum = 1 # 연산의 시작을 위한 1 (첫번째 자리를 그대로 곱하기 위해)

    if number == 0:
        break
    else:
        ans.append(number) # number를 첫번째 인덱스로 추가.

    

    while number >= 10:

        for num in f"{number}": # 문자열로 만들어서 쪼개주기
           
            xnum *= int(num) # 1 X 첫번째, 다음 반복에서 X 두번째 ...

        ans.append(xnum)

        number = xnum

        xnum = 1 # 새로 시작하는 반복에서 xnum의 잔재를 없애준다. 다시 초기화

    numdict[ans[0]] = ans

    

for number in numbers:
    if number == 0:
        break  # 입력시 0이 마지막에 들어가므로, 마지막에 오는 0을 기준 break

    else: # 아니면 그냥 진행하고, 리스트로 불리는 result를 
        result = numdict[number] 
        print(*result) #여기서 언패킹