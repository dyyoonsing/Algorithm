# 백준 11000. 강의실 배정

# 수강신청의 마스터 김종혜 선생님에게 새로운 과제가 주어졌다. 
# 김종혜 선생님한테는 Si에 시작해서 Ti에 끝나는 N개의 수업이 주어지는데, 최소의 강의실을 사용해서 모든 수업을 가능하게 해야 한다. 
# 참고로, 수업이 끝난 직후에 다음 수업을 시작할 수 있다. (즉, Ti ≤ Sj 일 경우 i 수업과 j 수업은 같이 들을 수 있다.)
# 수강신청 대충한 게 찔리면, 선생님을 도와드리자!

# 입력
# 첫 번째 줄에 N이 주어진다. (1 ≤ N ≤ 200,000)
# 이후 N개의 줄에 Si, Ti가 주어진다. (0 ≤ Si < Ti ≤ 109)

# Python heapq 모듈로 해결
import heapq

n = int(input())
classTimeList = []

for i in range(n) :
    classTimeList.append(list(map(int, input().split()))) 

classTimeList.sort()

classroomList = []
heapq.heappush(classroomList, classTimeList[0][1])

for i in range(1, n) :
    if classTimeList[i][0] < classroomList[0] : 
        # 수업 시작 시간이 현재 젤 빨리 끝나는 강의실보다 이른 경우 => 새로 강의실 하나 추가
        heapq.heappush(classroomList, classTimeList[i][1])
    else :
        heapq.heappop(classroomList)
        heapq.heappush(classroomList, classTimeList[i][1])

print(len(classroomList))


"""

# 시간 초과 나옴! ㅠ
n = int(input())
classTimeList = []
classroomList = [0]

for i in range(n) :
    classTimeList.append(list(map(int, input().split())))  


for classTime in classTimeList : 
    flagNoRoom = True
    for num in range(len(classroomList)) : 
        if classTime[0] >= classroomList[num] : 
            classroomList[num] = classTime[1]
            flagNoRoom = False
            break
    if flagNoRoom :
        classroomList.append(classTime[1])     


print(len(classroomList))

"""

