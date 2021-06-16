import math
def interpolationSearch(S,x):
  low = 0
  high= len(S)-1
  location= -1
  if S[low] <=x and x <= S[high]:
     while (low <=high and location== -1) :
        denominator = S[high] - S[low]
        if(denominator ==0):
            mid = low
        else:
            mid = low + math.floor(((x - S[low])*(high-low))/denominator)
        print("mid:",mid)
        if x == S[mid]:
            location= mid

        elif x <S[mid]:
            high = mid - 1
        else:
            low = mid + 1
  return location



S = [1,2,3,4,5,6,7,8,9,100]
x = 10
print(S)
print("Location of %d is %dth" % (x, interpolationSearch(S,x)))
