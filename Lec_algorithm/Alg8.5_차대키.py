s=[2,6,4,8,10,3,7,1]
a={}
while(len(s)>1):
  t=list()

  for i in range(0,len(s),2):
    if s[i]>s[i+1]:
      t.append(s[i])
      if(s[i] in a):
              a[s[i]]+=[s[i+1]]
      else:
        a[s[i]]=[s[i+1]]

    else:
      t.append(s[i+1])
      if( s[i+1] in a):
        a[s[i+1]] += [s[i]]
      else:
        a[s[i+1]]=[s[i]]


  print(a)
  print(t)
  s=t[:]

winner = t[:]
print(winner[0])
print(a[winner[0]])
print("second =", max(a[winner[0]]))
