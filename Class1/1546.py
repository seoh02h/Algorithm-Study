n = int(input())
scores = list(map(int, input().split()))
max = max(scores)
new_scores= list()
for i in scores:
    tmp = i/max * 100
    new_scores.append(tmp)

print(sum(new_scores)/n)