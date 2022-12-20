
# schedule = int(input())
scheduleList = []

# for i in range(schedule) :
#     scheduleList.append(list(map(int, input().split())))
schedule = 5
scheduleList = [[1, 9], [8, 9], [4, 6], [3, 5], [2, 5]]
print(scheduleList)

sortedList = sorted(scheduleList, key = lambda y : (y[0], -y[1]))
biggestNum = sorted(scheduleList, key = lambda y : -y[1])[0][1]

 
week = [0 for x in range(biggestNum)]
print(week)

for i in range(len(sortedList)) :
    for cntSc in range(sortedList[i][0], sortedList[i][1] + 1) :
        week[cntSc - 1] += 1

print(week)

strWeek = "".join(str(x) for x in week)
print(strWeek)
weekList = strWeek.split("0")
print(weekList)

totalSpace = 0
for i in weekList :
    width = len(i)
    heightList = sorted(list(i))
    height = heightList[len(i)-1]
    print(width, height)
    totalSpace += width*int(height)

print(totalSpace)