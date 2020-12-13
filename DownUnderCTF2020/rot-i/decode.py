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