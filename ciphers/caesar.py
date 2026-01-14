import ciphers._global as globalVar

name = "Caesar Cipher"
desc = "Standard Caesar Cipher, the one that started it all"

def cipher(plain_text, encode, demo):
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

		if not char.isalpha():
			totalStr += char
			continue

		base = globalVar.getOffset(char)

		charOffset = offset
		charOffset += (ord(char) - base)

		totalStr += chr(base + (charOffset) % 26)

	if demo:
		print(f"{globalVar.terminal.Text.Colors.BLUE}How to do the cipher:{globalVar.terminal.Text.RESET}")
		print("For every character in plain text...")
		print("\tGet the character's index (ie: a->0)")
		print("\tGet the offset character by doing index + offset")
		if encode:
			print("\tIe: 'Hello' with an offset of 2")
			print("\t\tH -> J")
			print("\t\te -> g")
			print("\t\tl -> n")
			print("\t\tl -> n")
			print("\t\to -> q")
		else:
			print("\tIe: 'Jgnnq' with an offset of 2 (inverted to decode, so -2)")
			print("\t\tJ -> H")
			print("\t\tg -> e")
			print("\t\tn -> l")
			print("\t\tn -> l")
			print("\t\tq -> o")

	return totalStr