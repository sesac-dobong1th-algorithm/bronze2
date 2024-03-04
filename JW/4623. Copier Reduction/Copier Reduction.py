import sys

while True:
    try:
        n = list(map(int, sys.stdin.readline().split()))

        if not n:  # 입력이 더 이상 없으면 종료
            break

        try:
            a = int(min([max(n[2:]) / max(n[:2]), min(n[2:]) / min(n[:2])]) * 100)
            if a > 100:
                print(f"100%")
            elif a > 1:
                print(f"{a}%")
            else:
                print("1%")
        except Exception as e:
            break

    except Exception as e:
        break