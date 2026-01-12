import ciphers._global as globalVar

name = "Vigenère Cipher"
desc = "Standard Vigenère Cipher"

def cipher(plain_text, encrypt):
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

		txtBase = globalVar.UPPER_OFFSET
		keyBase = globalVar.UPPER_OFFSET
		if not char.isupper():
			txtBase = globalVar.LOWER_OFFSET
		
		if not key[index].isupper():
			keyBase = globalVar.LOWER_OFFSET

		p = ord(char) - txtBase
		k = ord(key[index]) - keyBase
		nChar = 0
		if encrypt:
			nChar = (p + k) % globalVar.TOTAL_CHAR
		else:
			nChar = (p - k) % globalVar.TOTAL_CHAR

		totalStr += chr(nChar + txtBase)

		index += 1
		if index >= len(key):
			index = 0
	
	return totalStr