import ciphers._global as globalVar

name = "Vigenère Cipher"
desc = "Standard Vigenère Cipher"

def cipher(plain_text, encode):
	totalStr = ""

	key = input("Input Key:  ")

	index = 0
	for char in plain_text:
		if char == " ":
			totalStr += " "
			continue
		if not char.isalpha():
			totalStr += char
			continue

		txtBase = globalVar.getOffset(char)
		keyBase = globalVar.getOffset(key[index])

		p = ord(char) - txtBase
		k = ord(key[index]) - keyBase
		nChar = 0
		if encode:
			nChar = (p + k) % globalVar.TOTAL_CHAR
		else:
			nChar = (p - k) % globalVar.TOTAL_CHAR

		totalStr += chr(nChar + txtBase)

		index += 1
		if index >= len(key):
			index = 0
	
	return totalStr