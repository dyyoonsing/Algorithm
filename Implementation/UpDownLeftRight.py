# 입력조건 
# 5 
# R R R U D D

# 출력조건
# 3 4

from tracemalloc import start


mapSize = int(input())
moveList = input().split()
startSpot = [1,1]

for i in moveList :
    if i == 'L' and startSpot[1] > 1 :
        startSpot[1] -= 1
    elif i == 'R' and startSpot[1] < 5 :
        startSpot[1] += 1
    elif i == 'U' and startSpot[0] > 1 :
        startSpot[0] -= 1
    elif i == 'D' and startSpot[0] < 5 :
        startSpot[0] += 1

print(*startSpot) 