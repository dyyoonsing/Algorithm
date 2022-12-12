# 어떤 수 N이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 수행 => 최소 횟수 구하기
# - N에서 1을 뺀다
# - N을 K로 나눈다 (N이 K로 나누어 떨어질떄만 가능)

n, k = map(int, input("숫자 2개 입력 : ").split())

# N이 K로 나누어떨어질때까지 -1

cnt = 0

# while True:
#     if(n % k == 0) :
#         n /= k
#     else :
#         n -= 1
#     cnt += 1
#     if(n == 1) : 
#         break

# n이 k의 배수가 되도록!
while True :
    target = (n // k) * k
    cnt += n - target
    n = target
    if n < k :
        break
    cnt += 1
    n /= k

cnt += (n-1)

print(cnt)