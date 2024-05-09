s1 = "abcde"
d = {}
for i in  range (len(s1)):
    d[s1[i]] = d.get(s1[i], 0) +1
print(d)