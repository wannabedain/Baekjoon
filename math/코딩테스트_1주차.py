# 10430 나머지

A,B,C = map(int, input().split())

print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print(((A%C) * (B%C))%C)





# n의 수 중에서 1로만 이루어진 수 찾기. 그 중에서 가장 작은 수 -> 자리 수 

while True:
    try:
        x = int(input())
    except EOFError:
        break
    if x == 1:
        print('1')
        continue
    num = 1
    cnt = 1
    while True:
        num = num * 10 + 1
        cnt += 1
        if (num % x) == 0:
            print(cnt)
            break



# 1037번 약수
## A는 1이 아니고, N이 아님. 

n = int(input())  # 진짜 약수의 개수
divisors = list(map(int, input().split()))  # 진짜 약수
divisors.sort()

result = divisors[0] * divisors[-1]
print(result)



# 17427 약수의 합
## x = 5일 때 , 약수 1은 5개, 2는 2개, 3,4,5는 1개

## 자연수 N이 주어졌을 때, g(N)은?

''' 시간초과
x = int(input())
num = 0

for i in range(x):
    for j in range(1, i):
        if i % j == 0:
            num += j

print(num)
'''

n = int(input())

sum = 0
for i in range(1, n+1):
    sum += (n//i)*i

print(sum)





#17425 위의 것과 똑같이 풀면 -> 시간초과 X
'''
import sys
input=sys.stdin.readline

n = int(input())

for i in range(n):
    sum_ = 0
    a = int(input())
    for j in range(1, a+1):
        sum_ += (a//j)*j
    print(sum_)
'''

# N은 N의 약수의 배수로 이루어져있기 때문에 이를 이용하여 DP 배열을 만들 수 있음
# 최대값 설정

import sys

# 최대값 설정
MAX = 1000000

# 각 인덱스마다 약수의 합을 담아 놓을 배열 초기화
dp = [0] * (MAX + 1)
# 각 인덱스까지 누적합을 담을 배열 초기화
s = [0] * (MAX + 1)

for i in range(1, MAX + 1): #1부터 최대값까지
    j = 1 # i에 곱할 j를 선언
    while i * j <= MAX: # i * j 값이 최대값이 넘지 않을 때까지
        # dp배열의 인덱스인 i의 배수에 i 값을 더해준다. 
        dp[i * j] += i #예를들면 3*j의 해당하는 값들은 3을 무조건 약수로 가지기 때문에 3을 더해준다 
        j += 1 #j값 증가
    s[i] = s[i - 1] + dp[i] #해당 dp[i]의 값 까지 더한 누적합을 s배열에 넣어준다.

t = int(input()) #테스트 케이스 개수 입력

for _ in range(t):
    a = int(sys.stdin.readline())
    sys.stdout.write(str(s[a])+"\n")





# 2609 - 최대공약수와 최소공배수
# 유클리드 호제법 : a & b의 최대 공약수는 b & a를 b로 나눈 나머지의 최대공약수와 같다
import sys
data = list(int, sys.stdin.readline()).sort()

for i in range(data[0]):
    if data[0] % i == 0 




# 소수 구하기
import math
M, N = map(int, input().split())    # M : 시작 수    /     N : 종료 수
A = [0] * (N+1)


for i in range(2, N+1):
    A[i] = i

for i in range(2, int(math.sqrt(N)) + 1):
    if A[i] == 0 :
        continue
    for j in range(i + i, N + 1, i)  :  # 배수 지우기
         A[j] = 0

for i in range(M, N + 1):
    if A[i] != 0 :
        print(A[i])


