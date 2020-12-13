#!/usr/bin/python3

import pickle

flag = ""

with open('data', 'rb') as f:
    unpack = pickle.load(f)

for i in range(1, len(unpack)):
    try:
        flag += chr(unpack[i])
    except:
        flag += unpack[i]

print(flag)
