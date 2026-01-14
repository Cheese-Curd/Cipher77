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

def cipher(plain_text, encode, demo):
	totalStr = ""

	letterA = input("Input Letter A: ")
	letterB = input("Input Letter B: ")

	translateTable = str.maketrans({
		"a": letterA,
		"b": letterB
	})

	if encode:
		for char in plain_text:
			if not char.isalpha():
				continue

			base = globalVar.getOffset(char)

			index = ord(char) - base

			pString = pattern[index]

			totalStr += f"{pString.translate(translateTable)} "
	else:
		for word in plain_text.split():
			pString = pattern_reverse.get(word.lower())

			decodeTable = str.maketrans({
				letterA: "a",
				letterB: "b"
			})

			# Make sure it's valid
			if pString == None:
				totalStr += f"{word} "
				continue

			char = pattern_reverse.get(word.lower().translate(decodeTable))

			if char:
				totalStr += char
			else:
				totalStr += f"{word} "

	if demo:
		print(f"{globalVar.terminal.Text.Colors.BLUE}How to do the cipher:{globalVar.terminal.Text.RESET}")
		print("This one is weirdddd....")
		print("For context, there is a whole conversion table")
		print("\ta->aaaaa")
		print("\tb->aaaab")
		print("\tc->aaaba")
		print("\tEtc.")
		if encode:
			print("For every character in plain text...")
			print("\tJust convert it to use that table, and change a & b to be what you put in")
			print("\tHonestly, this one is just annoying to code, not really encode")
			print("\tJust make sure to add a space at the end of each 'letter'")
		else:
			print("For every word in cipher text...")
			print("\tIt's actually split by each 'space'")
			print("\tJust like encoding, more annoying to code than to actually decode.")
			print("\tConvert 'a' & 'b' to be whatever letters you put in.")
		print("\tThis cannot have 'multiple' words as it doesn't have any splitter.")

	return totalStr