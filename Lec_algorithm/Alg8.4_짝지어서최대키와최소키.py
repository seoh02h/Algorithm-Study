s=[2,6,4,8,10,3,7,1,5,9]
n= len(s)

if (s[0]<s[1]):
  small =s[0]
  large=s[1]
else:
  small = s[1]
  large=s[0]
for i in range(2,n,2):
  if s[i]<s[i+1]:
     if s[i]<small:
        small =s[i]
     if s[i+1]> large:
        large=s[i+1]
  else:
     if s[i+1]<small:
        small =s[i+1]
     if s[i]> large:
        large=s[i]
print(small, large)
