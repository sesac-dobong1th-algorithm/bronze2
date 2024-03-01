'''
sudo code
5694번 Bingo!
https://www.acmicpc.net/problem/5694
 (1 ≤ N ≤ 90) , (2 ≤ B ≤ N + 1).  (0 ≤ bi ≤ N)
N: TARGET, 
B: 가방에 남아 있는 공의 수
두 줄 입력 N: 
N , B
B_1 B_2 ....


0 0 0 0 => END_POINT

RESULT => 
두수 뺄셈으로 N까지 모두 표현가능 -> Y
ELSE : N

set을 활용 겹친거 제거, 인자확인은 in으로 돌림.
'''

while(True):
  n , b = map(int, input().split())
  if (n == 0) and (b==0):
      break
  b_list = list(map(int, input().split()))
  b_list.sort()
  minus_list = list()
  # minus_list 구하기
  for index in range(b):
      for item in b_list:
          minus_list.append(abs(b_list[index] - item))
  #겹친거 제거
  minus_list = list(set(minus_list))
  
  # 인자확인
  for num in range(n+1):
      if num not in minus_list:
          print('N')
          break
      if num == n:
          print('Y')