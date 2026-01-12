import ciphers._global as globalVar

name = "Bacon Cipher"
desc = "Offbrand Binary"

pattern = (
	"aaaaa",
	"aaaab",
	"aaaba",
	"aaabb",
	"aabaa",
	"aabab",
	"aabba",
	"aabbb",
	"abaaa",
	"abaaa",
	"abaab",
	"ababa",
	"ababb",
	"abbaa",
	"abbab",
	"abbba",
	"abbbb",
	"baaaa",
	"baaab",
	"baaba",
	"baabb",
	"baabb",
	"babaa",
	"babab",
	"babba",
	"babbb",
)

pattern_reverse = {word.lower(): chr(ord('a') + i) for i, word in enumerate(pattern)}

def cipher(plain_text, encode):
	totalStr = ""

	letterA = input("Input Letter A: ")
	letterB = input("Input Letter B: ")

	translateTable = str.maketrans({
		"a": letterA,
		"b": letterB
	})

	if encode:
		for char in plain_text:
			base = globalVar.getOffset(char)

			index = ord(char) - base

			pString = pattern[index]

			totalStr += f"{pString.translate(translateTable)} "
	else:
		for word in plain_text.split():
			pString = pattern_reverse.get(word.lower())

			# Make sure it's valid
			if pString == None:
				totalStr += f"{word} "
				continue

			char = pString.translate(translateTable)

			if char:
				totalStr += char
			else:
				totalStr += f"{word} "

	return totalStr