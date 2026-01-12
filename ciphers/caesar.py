import ciphers._global as globalVar

name = "Caesar Cipher"
desc = "Standard Caesar Cipher, the one that started it all"

def cipher(plain_text, encode):
	offset = 0
	while True:
		try:
			offset = int(input("Input Offset: "))
			break
		except:
			print("Input valid offset.")

	totalStr = ""
	
	if not encode:
		offset = -offset

	for char in plain_text:
		if char == " ":
			totalStr += " "
			continue
		if not char.isalpha():
			totalStr += char
			continue

		if char == " ":
			totalStr += " "
			continue
		if not char.isalpha():
			totalStr += char
			continue

		base = globalVar.UPPER_OFFSET
		if not char.isupper():
			base = globalVar.LOWER_OFFSET


		charOffset = offset
		charOffset += (ord(char) - base)

		totalStr += chr(base + charOffset)

	return totalStr