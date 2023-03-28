# [예제 4-1] 상화좌우
'''
- N x N 크기의 정사각형 공간

- 가장 왼쪽 위 좌표는 (1,1) / 가장 오른쪽 아래의 좌표는 (N,N)
- 시작좌표는 항상 (1,1)
- 'L'은 왼쪽, 'R'은 오른족, 'U'은 위로, 'D'은 아래로
- 최종적으로 도달할 지점의 좌표를 구하라
'''

n = int(input())
plans = input().split()

x, y = 1, 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans :
  for i in range(len(move_types)):
    if plan == move_types[i]:
      nx = x + dx[i] 
      ny = y + dy[i]

  if nx < 1 or ny < 1 or nx > n or ny > n:
    continue
  
  x, y = nx, ny

print(x, y)
