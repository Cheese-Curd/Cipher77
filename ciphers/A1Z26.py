import ciphers._global as globalVar

name = "A1Z26 Cipher"
desc = "The simpilist Cipher"

def cipher(plain_text, encode, demo):
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

	if demo:
		print(f"{globalVar.terminal.Text.Colors.BLUE}How to do the cipher:{globalVar.terminal.Text.RESET}")
		if encode:
			print("For every character in plain text...")
			print("\tGet the character's index (ie: a->0) and add one (a->1)")
			print("\tThen, add the seperator (ie: _)")
		else:
			print("For every 'word' (split by seperator ie: _) in cipher text...")
			print("\tGet the character index and subtract one (0->a)")
			print("\tThen, add that to the final string")

	return totalStr