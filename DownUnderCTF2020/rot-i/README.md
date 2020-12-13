# Rot-i - CRYPTO - 100pts.
## Description
ROT13 is boring!

## Attachments
> [challenge.txt](challenge.txt)
```
Ypw'zj zwufpp hwu txadjkcq dtbtyu kqkwxrbvu! Mbz cjzg kv IAJBO{ndldie_al_aqk_jjrnsxee}. Xzi utj gnn olkd qgq ftk ykaqe uei mbz ocrt qi ynlu, etrm mff'n wij bf wlny mjcj :).
```

## Solution
The cipher is a ROT-n where, unlike the ROT13, the rotation `n` is given by the __position__ of the character in the string starting from 0.
So the 1st character wouldn't have any rotation, the 2nd would have 1, the 3rd 2 and so on.

To decode the message i wrote this simple python script:

```python3
#!/usr/bin/python3

alphabet = "abcdefghijklmnopqrstuvwxyz"
rot = 0
out = ""

with open('challenge.txt') as f:
	
	cipher = f.readline().lower()
	
	for c in cipher:
		if c in alphabet: out += alphabet[alphabet.find(c)-rot%26]
		else: out += c

		rot += 1

	print(out)
```
Output:
```
you've solved the beginner crypto challenge! the flag is ductf{crypto_is_fun_kjqlptzy}. now get out some pen and paper for the rest of them, they won't all be this easy :).
```
Flag: `DUCTF{crypto_is_fun_kjqlptzy}`
