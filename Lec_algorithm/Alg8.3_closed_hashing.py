# closed hashing data into 0 ... M-1
M=10

#conver d to integer.
# each char is convered to ascii code number
def hashing(data):
  hash_data =[-1 for i in range(0,M-1)]
  for d in data:
      s = 0
      for x in d:
         s+=ord(x)
      s = s%M
      hash_data[s]=d
  return hash_data

data =["abc", "name", "school", "KHU"]
print(hashing(data))
