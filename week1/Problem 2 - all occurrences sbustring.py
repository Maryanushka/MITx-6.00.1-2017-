ind = 1
count = 0
f = 'bob'
s='absuebobobobdkdkoewjwqefbob'
while ind >= 0:
    ind = s.find(f)
    if ind >= 0:
        count += 1
    s = s[ind+1:]
print(count)

# поиск всех вхождений подстроки