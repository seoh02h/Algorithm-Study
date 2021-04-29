'''
def sum1(s):
    result = 0
    for a in s:
        result += a
    return result
'''
def sum2(s):
    result = 0
    for i in range(len(s)):
        result += s[i]
    return result

s = [3, 5, 2, 1, 7, 9]
#answer = sum1(s)
answer = sum2(s)
print(answer)