# 숫자 카드 게임
# N행 X M열로 배치된 숫자 중 N행의 가장 작은 숫자가 젤 커야 한다

n, m = map(int, input("숫자 2 : ").split())

result = 0
for x in range(n) : 
    data = list(map(int, input(str(x) + "행의 숫자 " + str(m) + "개 : ").split()))
    minNum = min(data)
    result = max(result, minNum)

print(result)