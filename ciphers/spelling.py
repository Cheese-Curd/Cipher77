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
	"Victor"
)

NATO_REVERSE = {word.lower(): chr(ord('a') + i) for i, word in enumerate(NATO)}

name = "Spelling Alphabet"
desc = "Not really a cipher, but converts each letter into it's Vocal Form"

def cipher(plain_text, encode):
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
				totalStr += word

	return totalStr