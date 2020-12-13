# In a pickle - MISC - 200pts.
## Description
We managed to intercept communication between und3rm4t3r and his hacker friends.
However it is obfuscated using something.
We just can't figure out what it is.
Maybe you can help us find the flag?

## Attachments
###### [data](data)
```
(dp0
I1
S'D'
p1
sI2
S'UCTF'
p2
sI3
S'{'
p3
sI4
I112
sI5
I49
sI6
I99
sI7
I107
sI8
I108
sI9
I51
sI10
I95
sI11
I121
sI12
I48
sI13
I117
sI14
I82
sI15
I95
sI16
I109
sI17
I51
sI18
I53
sI19
I53
sI20
I52
sI21
I103
sI22
I51
sI23
S'}'
p4
sI24
S"I know that the intelligence agency's are onto me so now i'm using ways to evade them: I am just glad that you know how to use pickle. Anyway the flag is "
p5
s.
```

## Solution
After taking a look at `data` i noticed the bottom sentence `I am just glad that you know how to use pickle`.
Considering that and the challenge name, i knew that pickle was required to decode the data, so i wrote this simple script:

```python3
#!/usr/bin/python3

import pickle

flag = ""

with open('data', 'rb') as f:
    unpack = pickle.load(f)

print(unpack)
```

Output:
```
{1: 'D', 2: 'UCTF', 3: '{', 4: 112, 5: 49, 6: 99, 7: 107, 8: 108, 9: 51, 10: 95, 11: 121, 12: 48, 13: 117, 14: 82, 15: 95, 16: 109, 17: 51, 18: 53, 19: 53, 20: 52, 21: 103, 22: 51, 23: '}', 24: "I know that the intelligence agency's are onto me so now i'm using ways to evade them: I am just glad that you know how to use pickle. Anyway the flag is "}
```
The unpacked data was a dictionary with some of its value being integers, so i tried converting those `int` to `char`.
To do that i modified the previous code:

```python3
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
```
Output: `DUCTF{p1ckl3_y0uR_m3554g3}`
