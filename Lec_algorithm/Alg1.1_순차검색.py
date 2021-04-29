def seqsearch(s, x):
    loc = 0
    while(loc < len(s) and s[loc] != x):
        loc += 1
    if loc >= len(s):
        loc = -1
    return loc

s = [3, 5, 2, 1, 7, 9]
loc = seqsearch(s, 4)
print(loc)