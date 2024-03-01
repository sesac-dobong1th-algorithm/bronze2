'''
문제가 설명이 세상 쉽지 않네요.

핵심 요약느낌으로 가면
1. 처음수 N은 내가 1번부터 표현할 수
2. 이후 뽑은 B는 내가 뽑을수있는 공의 갯수
3. 마지막으로 뽑는 BI 는 B만큼 뽑는데 이 숫자를 가지고 '어떻게든(두숫자를 잘빼서입니다)' N을 0부터 도출

조건
N은 1<= N <=90
B는 2<= B <=N+1
0<= BI <= N

조건 있기전에는 걍 N번만큼 연산을 N!만큼 모든수 빼서1~6있음 종료하려했는데 
행동에 제약이있음

여기서 조금 나아가서 뽑은 공의 조합으로 만들수있는 빼기들의 집함을 생성

중복 불허하는 set()사용

루프를 돌면서 현재 루프의 요소와 모든 요소를 비교하여 차이를 구해야 함(이중 포문!!)

'''
# 주어진 N, B, balls_in_bag에 대해 모든 숫자를 표현할 수 있는지 여부를 판단하는 함수
def is_possible_to_call_out(N, B, balls_in_bag):
    # 모든 숫자를 포함하는 집합 생성
    # 내장 자료형 중에 list set dicionary가 있는데 set이 젤 빠름(중복 불허 동일값 있음 저장안함)
    all_numbers = set(range(N + 1))
    # print(all_numbers)
    # 뽑은 공으로부터 가능한 모든 차를 생성
    possible_differences = set()
    for i in range(B):
        for j in range(i, B):
            possible_differences.add(abs(balls_in_bag[i] - balls_in_bag[j])) # 현재번째 요소와 모든 요소 비교

    # 모든 숫자를 뽑을 수 있는지 확인
    # 이번에 set 공부하면서 매서드목록 보면서 처음 알았습니다
    # set 간의 비교는 메서드로 하더라구요 union()같은 합집합 등으로 비교합니다.
    # https://withcoding.com/77
    '''
    is로 시작하는 함수는 True 또는 False를 리턴한다. (bool 값)

    isdisjoint() - 두 집합이 공통 원소를 갖지 않는가?

    issubset() - 부분집합(subset)인가?

    issuperset() - 확대집합(superset)인가?

    즉 부분 집합
    '''
    # return all_numbers.issubset(possible_differences)
    return all_numbers==possible_differences


# 입력을 받고 결과 출력
while True:
    # N과 B를 입력 받음 map()은 리스트나 튜플로 값 받기!
    N, B = map(int, input().split())
    
    # 입력이 0 0이면 루프 종료
    if N == 0 and B == 0:
        break
    
    # B 개의 공을 리스트로 입력 받음 두번째 입력 공들을 받기
    balls_in_bag = list(map(int, input().split()))

    # 함수 호출하여 결과를 얻고 출력
    result = is_possible_to_call_out(N, B, balls_in_bag)
    if result:
        print("Y")
    else:
        print("N")
