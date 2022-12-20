schedule = int(input())
scheduleList = []

for i in range(schedule) :
    scheduleList.append(list(map(int, input().split())))

sortedList = sorted(scheduleList, key = lambda y : (y[0], -y[1]))
biggestNum = sorted(scheduleList, key = lambda y : -y[1])[0][1]

 
week = [0 for x in range(biggestNum)]

for i in range(len(sortedList)) :
    for cntSc in range(sortedList[i][0], sortedList[i][1] + 1) :
        week[cntSc - 1] += 1

strWeek = "".join(str(x) for x in week)
weekList = strWeek.split("0")

totalSpace = 0
for i in weekList :
    if len(i) > 0 :
        width = len(i)
        heightList = sorted(list(i))
        height = heightList[len(i)-1]
        totalSpace += width*int(height)

print(totalSpace)



'''
# schedule = i
schedule = int(input())
scheduleList = []

for i in range(schedule) :
    scheduleList.append(list(map(int, input().split())))

sortedList = sorted(scheduleList, key = lambda y : (y[0], -y[1]))
biggestNum = sorted(scheduleList, key = lambda y : -y[1])[0][1]

 
week = [0 for x in range(biggestNum)]

for i in range(len(sortedList)) :
    for cntSc in range(sortedList[i][0], sortedList[i][1] + 1) :
        week[cntSc - 1] += 1

strWeek = "".join(str(x) for x in week)
weekList = strWeek.split("0")

totalSpace = 0
for i in weekList :
    if len(i) > 0 :
        width = len(i)
        heightList = sorted(list(i))
        height = heightList[len(i)-1]
        totalSpace += width*int(height)

print(totalSpace)
'''
