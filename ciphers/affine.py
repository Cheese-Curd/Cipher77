import ciphers._global as globalVar

name = "Affine Cipher"
desc = "Standard Affine Cipher"

def cipher(plain_text="", encode=False, demo=False):
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

		base = globalVar.getOffset(char)

		offset = 0
		charIndex = ord(char) - base
		if encode:
			offset = (aOffset * charIndex) + bOffset
		else:
			aOffset = pow(aOffset, -1, globalVar.TOTAL_CHAR) # Inverse A
			offset = aOffset * (charIndex - bOffset)

		offset = offset % globalVar.TOTAL_CHAR

		totalStr += chr(offset + base)

	if demo:
		print(f"{globalVar.terminal.Text.Colors.BLUE}How to do the cipher:{globalVar.terminal.Text.RESET}")
		print("For every character in plain text...")
		print("\tGet the character's index (ie: a->0)")
		if encode:
			print("\tGet the offset by doing (aOffset * charIndex) + bOffset")
		else:
			print("\tInverse the A Offset (aOffset^-1) % 26 (26 being letters in the alphabet)")
			print("\tGet the offset by doing aOffset * (charIndex - bOffset)")
		print("\tDo offset % 26, and add that offset character to the total string")
	
	return totalStr