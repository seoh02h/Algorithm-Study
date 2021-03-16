n = int(input())
words = [0]*n
for i in range(n):
    word = input()
    words[i]=word


words = list(set(words))

sort_words = list()
for i in words:
    sort_words.append((len(i),i))

sort_words = sorted(sort_words)
for len, word in sort_words:
    print(word)