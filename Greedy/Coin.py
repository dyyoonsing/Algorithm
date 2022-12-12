# 거스름돈
# 손님에게 거슬러 줘야 할 돈이 N원일 때 거슬러 줘야 하는 동전의 최소 개수?
# 동전 : 500, 100, 50, 10

moneyLeft = int(input("남은 돈 : "))
coinArr = [500, 100, 50, 10]

answer = 0
money = moneyLeft
for x in coinArr :
    while money // x > 0 :
        answer += 1
        money -= x

print("동전 개수 : " + str(answer) )