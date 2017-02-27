

# def find_longest_substring_in_alphabetical_order(s):
#     groups = []
#     cur_longest = ''
#     prev_char = ''
#     for c in s.lower():
#         if prev_char and c < prev_char:
#             groups.append(cur_longest)
#             cur_longest = c
#         else:
#             cur_longest += c
#         prev_char = c
#     print(max(groups, key=len) if groups else s)
#
# find_longest_substring_in_alphabetical_order('azcbobobegghakl')

s = 'azcbobobegghakl'
r,p,t = '','',''
for c in s:
    if p <= c:
        t += c
        p = c
    else:
        if len(t) > len(r):
            r = t
        t,p = c,c
if len(t) > len(r):
    r = t
print( 'Longest substring in alphabetical order is: ' + r)


# start = 0
# end = 0
# temp = ""
# while end+1 <len(s):
#     while end+1 <len(s) and s[end+1] >= s[end]:
#         end += 1
#     if len(s[start:end+1]) > len(temp):
#         temp = s[start:end+1]
#     end +=1
#     start = end
# print("longest ordered part is: "+temp)
# fin=""
# s_pos =0
# while s_pos < len(s):
#     n=1
#     lng=" "
#     for c in s[s_pos:]:
#         if c >= lng[n-1]:
#             lng+=c
#             n+=1
#         else :
#             break
#     if len(lng) > len(fin):
#         fin= lng
#     s_pos+=1
# print( "Longest string: " + fin)