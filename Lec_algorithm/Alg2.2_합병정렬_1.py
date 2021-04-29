# [m:n] : 인덱스가 m인 데이터부터 인덱스가 n-1인 데이터까지를 표현
# m이 없을 경우 : 처음부터
# n이 없을 경우 : 끝까지
a=[4,1,5,9,10]
h=3
leftHalf=a[:h]
rightHalf=a[h:]
print(leftHalf)
print(rightHalf)


# 리스트는 mutable : 값을 바꿀 수 있다
# b = a : 리스트 a를 b라고도 나타낼 수 있다
# c = a[:] : 리스트 a를 리스트 c에 복사한다
a=['a','b','c','d','e']
print(a[1:3])
print(a[:3])
print(a[3:])
