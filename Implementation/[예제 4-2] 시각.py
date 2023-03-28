# [예제 4-2] 시각
'''
- 정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램
- 1을 입력했을 때, 3이 하나라도 포함되어 있으므로 세어야 함


****** 단순 시, 분, 초에 대한 경우의 수로, 3중 반복문 이용해서 계산
'''

N = str(input())

count = 0

for i in range(int(N)+1) : 
  for j in range(60) :
    for z in range(60) :
      time = str(i) + str(j) + str(z)
      if '3' in time : count += 1

print(count)