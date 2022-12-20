# Knight 
'''
8 * 8 의 체스판에서 위치를 알려주면 움직일 수 있는경우의 수 구하기
입력값
a1
출력값 
2

좌표의 경우 움직이는 경우의 수 튜플로 만들어놓기! (튜플 움직이지 않는 값)
'''

# 움직일 수 있는 경우 (x, y)
move = [(1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]

# 문자 숫자로 바꾸기?

mySpot = list(input())
mySpot = [int(ord(mySpot[0])) - 96, int(mySpot[1])]

print(mySpot)

moveCnt = 0
for m in move :
    if mySpot[0] + m[0] > 0 and mySpot[0] + m[0] <= 8 and mySpot[1] + m[1] > 0 and mySpot[1] + m[1] <= 8 :
        moveCnt += 1

print(moveCnt)