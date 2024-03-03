while True:
    # 네 개의 정수를 입력받음
    A, B, C, D = map(int, input().split())

    # 모든 입력값이 0이면 반복 종료
    if A == B == C == D == 0:
        break

    # A와 B를 비교하여 큰 값이 A가 되도록 교환
    if A < B:
        A, B = B, A

    # C와 D를 비교하여 큰 값이 C가 되도록 교환
    if C < D:
        C, D = D, C

    # 이분 탐색을 위한 시작과 끝 값 설정
    start, end = 1, 100
    result = 0

    # 이분 탐색
    while start <= end:
        mid = (start + end) // 2

        # 조건을 만족하면 mid 값을 결과로 저장하고 범위를 오른쪽으로 이동
        if A * mid <= C * 100 and B * mid <= D * 100:
            start = mid + 1
            result = mid
        else:
            # 조건을 만족하지 못하면 범위를 왼쪽으로 이동
            end = mid - 1

    # 결과 출력
    print(f'{result}%')
