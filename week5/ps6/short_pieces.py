shift = 3
alphabet = "abcdefghijklmnopqrstuvwxyz"

shifted = alphabet[shift:] + alphabet[:shift]
print(shifted)

import string

l_keys = list(string.ascii_lowercase)
l_values = list(string.ascii_lowercase)
shift_l_values = l_values[shift:]  + l_values[:shift]

u_keys = list(string.ascii_uppercase)
u_values = list(string.ascii_uppercase)
shift_u_values = u_values[shift:]  + u_values[:shift]

full_k = l_keys + u_keys
full_v = shift_l_values + shift_u_values
print(full_v)
d = dict(zip(full_k, full_v))

print(d)


text = 'abc'
n_msg = []
for i in text:
    if i in d.keys():
        n_msg.append(d[i])
print(''.join(n_msg))
