# 정수 N이 입력되면 00시 00분 00초 ~ N시 59분 59초까지 3이 포함된 모든 경우의 수 구하기 (0 <= n <= 23)

n = int(input())

# 0 ~ 59까지 3이 포함된 경우 ? 1의 자리 : 6개 + 30~39 : 10개 - 33 : 1개 = 15개
# 0시 ~ 23시까지 3이 포함된 경우? 3 13 23시
minSecCnt = 0
for i in range(59) : 
    if '3' in str(i) :
        minSecCnt += 1

print(minSecCnt)

hourCnt = 0
for j in range(n + 1) : 
    if '3' in str(j) : 
        hourCnt += 1

print(hourCnt)
answer = minSecCnt * minSecCnt * hourCnt

print(answer)