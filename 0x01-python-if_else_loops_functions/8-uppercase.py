#!/usr/bin/env python3
def uppercase(str):
	for alf in range(len(str)):
		aux = ord(str[alf])
		if aux >= 97 and aux <= 122:
			aux -=32
		print("{:c}".format(aux), end = "")
	print()
