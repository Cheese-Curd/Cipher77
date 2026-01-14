import ciphers._global as globalVar

name = "Vigenère Cipher"
desc = "Standard Vigenère Cipher"

def cipher(plain_text, encode, demo):
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
	
	if demo:
		print(f"{globalVar.terminal.Text.Colors.BLUE}How to do the cipher:{globalVar.terminal.Text.RESET}")
		print("For every character in plain text...")
		print("\tp: The Character's index (ie: a->0)")
		print("\tk: The Key's Character index (ie: a->0)")
		print("")
		if encode:
			print("\tThen, you want to do (p + k) % 26 (26 being the letters in the alphabet)")
		else:
			print("\tThen, you want to do (p - k) % 26 (26 being the letters in the alphabet)")
		print("\tThat gives you the character to add to the finished string.")

	return totalStr