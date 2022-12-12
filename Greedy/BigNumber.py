# 큰 수의 법칙

# 크기 N의 배열이 있을 때, M번 더하여 가장 큰 수 구하기. 단, 특정 인덱스의 숫자가 K번 초과하여 연속으로 더해질 수 없다

# 첫째 줄에 N(2 <= N <= 1,000), M(1 <= M <= 10,000), K(1 <= K <=10,000)의 자연수가 주어지며, 각 자연수는 공백으로 구분한다
# 둘째 줄에 N개의 자연수가 주어진다. 각 자연수는 공백으로 구분한다.  단, 각각의 자연수는 1 이상 10,000 이하의 수로 주어진다
# 입력으로 주어지느 K는 항상 M보다 작거나 같다.

# ex ) 
# 5 8 3
# 2 4 5 4 6

# n, m, k = map(int, input("숫자 3개 입력 : ").split())
# numberArr = list(map(int, input("배열 입력 : ").split()))

n, m, k = [5, 8, 3]
numberArr = [2, 4, 5, 4, 6]

numberArr.sort()
biggestNum = numberArr[n-1]
secondbiggestNum = numberArr[n-2]

biggestResult = 0

# (제일 큰 수 * K) + 두번째로 큰 수 => K+1
# M // (K+1)  *  ((제일 큰 수 * K) + 두번째로 큰 수) 
# M % (K+1) * 제일 큰 수

biggestResult = ((biggestNum * k) + secondbiggestNum) * (m // (k+1)) + (biggestNum * (m % (k+1)))

print(biggestResult)






