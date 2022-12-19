def makeSnail(snail, curNum, curSpot, curSnailSize, findNum, findNumSpot) :
    snailSize = len(snail)
    centerSpot = [snailSize//2, snailSize//2]
    maxNum, minNum = centerSpot[0] + curSnailSize // 2, centerSpot[0] - curSnailSize // 2
    curSpotX, curSpotY = curSpot[0], curSpot[1]

    for i in range(curNum, curSnailSize**2 + 1) :
        if findNum == i :
            findNumSpot = [curSpotX+1, curSpotY+1]
        
        snail[curSpotX][curSpotY] = i

        if curSpotX == minNum :
            if curSpotY == minNum : 
                curSpotX -= 1
            elif curSpotY < maxNum :
                curSpotY += 1
            elif curSpotY == maxNum :
                curSpotX += 1

        elif curSpotY == maxNum :
            if curSpotX < maxNum : 
                curSpotX += 1
            elif curSpotX == maxNum :
                curSpotY -= 1     

        elif curSpotX == maxNum :
            if curSpotY > minNum : 
                curSpotY -= 1
            elif curSpotY == minNum :
                curSpotX -= 1     

        elif curSpotY == minNum :
            if curSpotX > minNum : 
                curSpotX -= 1

    
    curSpot = [curSpotX, curSpotY]

    if curSnailSize == snailSize :
        return [snail, findNumSpot]
    else :
        return makeSnail(snail, curSnailSize**2 + 1, curSpot, curSnailSize + 2, findNum, findNumSpot)


n = int(input())
findNum = int(input())
snail = [[0 for col in range(n)] for row in range(n)]      
centerSpot = [n//2 ,n//2]
findNumSpot =[0,0]

answer = makeSnail(snail, 1, centerSpot, 1, findNum, findNumSpot)

for snailLoop in range(n) :
    print(*answer[0][snailLoop])
print(*answer[1])

#  ㅎㅎ 반대로함,,
#  def makeSnail(snail, snailN, startN, startSpot, qNum, numSpot) : 
#     maxNum = 4 * (snailN - 1)
#     maxNum += startN - 1
#     curSpot = startSpot
#     startSpotX, startSpotY = startSpot[0], startSpot[1]
#     endSpotX, endSpotY = startSpotX + snailN - 1, startSpotY + snailN - 1

#     # 마지막 하나만 남은 경우
#     if startN == maxNum :
#         snail[startSpotX][startSpotY] = startN
    
#     for i in range(startN, maxNum + 1) : 
#         snail[curSpot[0]][curSpot[1]] = i
#         if i == qNum : 
#             numSpot[0], numSpot[1] = curSpot[0], curSpot[1]
#         if curSpot[1] == startSpotY : 
#             if curSpot[0] >= startSpotX and curSpot[0] <= endSpotX :
#                 if curSpot[0] == endSpotX :
#                     curSpot[1] += 1
#                 else :
#                     curSpot[0] += 1
#         elif curSpot[0] == endSpotX :
#             if curSpot[1] >= startSpotY and curSpot[1] <= endSpotY :
#                 if curSpot[1] == endSpotY :
#                     curSpot[0] -= 1
#                 else :
#                     curSpot[1] += 1
#         elif curSpot[1] == endSpotY :
#             if curSpot[0] >= startSpotX and curSpot[0] <= endSpotX :
#                 if curSpot[0] == startSpotX :
#                     curSpot[1] -= 1
#                 else :
#                     curSpot[0] -= 1
#         elif curSpot[0] == startSpotX :
#             if curSpot[1] >= startSpotY and curSpot[1] <= endSpotY :
#                 if curSpot[0] == endSpotX :
#                     curSpot[0] += 1
#                 else :
#                     curSpot[1] -= 1 
    
#     if snailN == 1 or snailN == 2 :
#         return [snail, numSpot]
#     else :
#         startSpot = [startSpotX + 1, startSpotY + 1]
#         return makeSnail(snail, snailN-2, maxNum+1, startSpot, qNum, numSpot)

# n = int(input())
# qNum = int(input())
# snail = [[0 for col in range(n)] for row in range(n)]

# answer = makeSnail(snail, n, 1, [0,0], qNum, [0,0])


# for nIdx in range(n) : 
#     print(*answer[0][nIdx])

# print(answer[1])