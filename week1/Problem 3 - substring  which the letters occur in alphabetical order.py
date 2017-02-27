s = 'azcbobobegghakl'
l = len(s)
currentStr = s[0]
maxStr = s[0]

for i in range(1, l):
    if (s[i] >= s[i-1]):
        currentStr += s[i]
    else:
        currentStr = s[i]
    if (len(currentStr) > len(maxStr)):
        maxStr = currentStr
print(maxStr)
 # it works!!!!


