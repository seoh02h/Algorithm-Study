t = int(input())
for i in range(t):
    n, str = input().split()
    text = ''
    for s in str:
        text += s*int(n)
    print(text)