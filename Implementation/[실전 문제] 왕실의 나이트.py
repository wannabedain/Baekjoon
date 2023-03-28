# [실전 문제] 왕실의 나이트
'''
- 8 * 8 좌표 평면
- L자 형태로만 이동 / 정원 밖으로는 나갈 수 없음
- 2가지 경우로 이동할 수 O
  * 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동 
  * 수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동 

- [표현] 행 위치는 1부터 8 / 열 위치는 a부터 h


*** 경우의 수 : (2, 1) (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)
  - ord("a") = 97 이므로, 이걸로 정수형으로 바꿈
  - [예제 4-1] 상화좌우 / 앞의 문제랑 거의 똑같으 방식으로 품
'''


# ord("a")  # 번호 확인

input_data = str(input())

row = int(input_data[1])
col = ord(input_data[0]) - 96

count = 0

steps = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

for step in steps :
  next_col = col + step[0]
  next_row = row + step[1]

  if next_col < 1 or  next_col > 8 or  next_row < 1 or next_row > 8 :
    continue
  
  count += 1

print(count)