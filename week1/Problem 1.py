vowels = "aeiouAEIOU"
count =0

for index,c in enumerate(s):
    if c in vowels:
        count+=1
print(count)