import random

def insertion_sort(s):
   n = len(s)
   for i in range (1,n):
      x = s[i]
      j=i-1
      while j>=0 and s[j] > x:
        s[j+1]=s[j]
        j -= 1
      s[j+1]=x
   return s

def select(k,s):
  tempList=5*[0]
  mList =[]
  s1=[]
  s2=[]
  s3=[]
  if len(s) <50:
      insertion_sort(s)
      return s[k-1]
  else:
      for j in range(0,int(len(s)/5)):
         for p in range(0,5):
            tempList[p]=s[j*5+p]
         tempList = insertion_sort(tempList)
         mList.append(tempList[2])
      insertion_sort(mList)
      m = select( int(len(mList)/2),mList)
      for i in range(0,len(s)):
          if s[i]< m:
              s1.append(s[i])
          elif s[i]== m:
              s2.append(s[i])
          else:
              s3.append(s[i])

      if len(s1) >= k:
          return select(k,s1)
      elif len(s1)+len(s2) >= k:
          return m
      else:
          return select(k-len(s1)-len(s2), s3)
N=125   # 간단히 하기 위해 N의 지수값으로 설정
s=N*[0]
k=120

for i in range(0,N):
     s[i]=random.randint(1,1000)

print()
print("original")
print(s)
print()
print(k,"th element = ", select(k,s))

print()
print("sorted")
print(insertion_sort(s))
