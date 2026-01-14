import ciphers._global as globalVar

name = "A1Z26 Cipher"
desc = "The simpilist Cipher"

def cipher(plain_text, encode):
	seperator = input("Input Seperator: ")

	totalStr = ""

	if encode:
		for char in plain_text:
			if not char.isalpha():
				continue

			base = globalVar.getOffset(char)

			if len(totalStr) > 0:
				totalStr += seperator

			totalStr += str((ord(char) - base) + 1)
	else:
		upper = globalVar.getYesNo("Uppercase?")

		base = globalVar.UPPER_OFFSET
		if upper == False:
			base = globalVar.LOWER_OFFSET

		for word in plain_text.split(seperator):
			try:
				# Only do it if it's valid
				int(word)
			except:
				continue

			totalStr += chr((int(word) + base) - 1)
	
	return totalStr