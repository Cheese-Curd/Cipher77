import ciphers._global as globalVar

NATO = (
	"Alpha",
	"Bravo",
	"Charlie",
	"Delta",
	"Echo",
	"Foxtrot",
	"Golf",
	"Hotel",
	"India",
	"Juliett",
	"Kilo",
	"Lima",
	"Mike",
	"November",
	"Oscar",
	"Papa",
	"Quebec",
	"Romeo",
	"Sierra",
	"Tango",
	"Uniform",
	"Victor",
	"Whiskey",
	"X-ray",
	"Yankee",
	"Zulu"
)

NATO_REVERSE = {word.lower(): chr(ord('a') + i) for i, word in enumerate(NATO)}

name = "Spelling Alphabet"
desc = "Not really a cipher, but converts each letter into it's Vocal Form"

def cipher(plain_text, encode, demo):
	totalStr = ""

	if encode:
		for char in plain_text:
			if not char.isalpha():
				totalStr += "... "
				continue

			base = globalVar.getOffset(char)

			index = ord(char) - base

			totalStr += f"{NATO[index]} "
	else:
		for word in plain_text.split():
			char = NATO_REVERSE.get(word.lower())

			if char:
				totalStr += char
			else:
				if word == "...":
					word = " "
				totalStr += word
	
	if demo:
		print(f"{globalVar.terminal.Text.Colors.BLUE}How to do the cipher:{globalVar.terminal.Text.RESET}")
		print("This one is weirdddd....")
		print("For context, there is a whole conversion table")
		print("\ta->Alpha")
		print("\tb->Bravo")
		print("\tc->Charlie")
		print("\tEtc.")
		if encode:
			print("For every character in plain text...")
			print("\tJust convert it to use that table")
			print("\tI simply add a '...' to seperate words")
		else:
			print("For every word in cipher text...")
			print("\tIt's actually split by each 'space'")
		print("\tVery similar to the Bacon Cipher, just allows for word seperation")

	return totalStr