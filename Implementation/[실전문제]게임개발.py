

N, M = map(int, input().split())
x, y, d = map(int, input().split())

#맵array 만들기
array = []
for _ in range(M):
  array.append(list(map(int, input().split())))

#이동 시의 가중치
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

cnt = 1 #방문 칸 수
while True:
    array[y][x] = 'v'       #현재 위치를 방문 처리
        
    for i in range(5):     #방향을 바꿔가며 갈 곳 조사
            
        if i == 4:          #갈 곳이 없다면
          nx = x - dx[d]
          ny = y - dy[d]
            if array[ny][nx] == 1:  #뒤가 바다라면
                return print(cnt)   #종료
            else:                   #뒤가 방문했던 곳이라면 이동
                x, y = nx, ny
                break
                    
        #방향 바꾸기
        d -= 1
        if d < 0:
            d += 4
        #어디로 이동할지 미리 보는 nx,ny.
        nx = x + dx[d]
        ny = y + dy[d]
        if array[ny][nx] == 0:     #갈 수 있다면 이동.
            x, y = nx, ny
            cnt += 1
            break
