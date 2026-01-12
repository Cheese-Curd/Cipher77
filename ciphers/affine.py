import ciphers._global as globalVar

name = "Affine Cipher"
desc = "Standard Affine Cipher"

def cipher(plain_text="", encode=False):
	while True:
		try:
			aOffset = int(input("Input A Offset: "))
			bOffset = int(input("Input B Offset: "))

			break
		except:
			print("Input valid offset.")

	totalStr = ""

	for char in plain_text:
		if char == " ":
			totalStr += " "
			continue
		if not char.isalpha():
			totalStr += char
			continue

		base = globalVar.UPPER_OFFSET
		if not char.isupper():
			base = globalVar.LOWER_OFFSET

		offset = 0
		charIndex = ord(char) - base
		if encode:
			offset = (aOffset * charIndex) + bOffset
		else:
			aOffset = pow(aOffset, -1, globalVar.TOTAL_CHAR) # Inverse A
			offset = aOffset * (charIndex - bOffset)

		offset = offset % globalVar.TOTAL_CHAR

		totalStr += chr(offset + base)
	
	return totalStr