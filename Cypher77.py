import random
from os import system, name

UPPER_OFFSET = 65
LOWER_OFFSET = 97
TOTAL_CHAR   = 26

ASCII_TEXT = """
  /$$$$$$  /$$           /$$                                 /$$$$$$$$ /$$$$$$$$
 /$$__  $$|__/          | $$                                |_____ $$/|_____ $$/
| $$  \__/ /$$  /$$$$$$ | $$$$$$$   /$$$$$$   /$$$$$$            /$$/      /$$/ 
| $$      | $$ /$$__  $$| $$__  $$ /$$__  $$ /$$__  $$          /$$/      /$$/  
| $$      | $$| $$  \ $$| $$  \ $$| $$$$$$$$| $$  \__/         /$$/      /$$/   
| $$    $$| $$| $$  | $$| $$  | $$| $$_____/| $$              /$$/      /$$/    
|  $$$$$$/| $$| $$$$$$$/| $$  | $$|  $$$$$$$| $$             /$$/      /$$/     
 \______/ |__/| $$____/ |__/  |__/ \_______/|__/            |__/      |__/      
              | $$                                                              
              | $$                                                              
              |__/                                                              
"""

splashes = []
with open("splashes.txt", "r", encoding="utf-8") as file:
    splashes = [line.strip() for line in file]

loop = True

def clear():
    system("cls" if name == "nt" else "clear")

def vigenereCipher(plain_text, key, encrypt):
	global UPPER_OFFSET, LOWER_OFFSET, TOTAL_CHAR

	totalStr = ""

	index = 0
	for char in plain_text:
		if char == " ":
			totalStr += " "
			continue
		if not char.isalpha():
			totalStr += char
			continue

		txtBase = UPPER_OFFSET
		keyBase = UPPER_OFFSET
		if not char.isupper():
			txtBase = LOWER_OFFSET
		
		if not key[index].isupper():
			keyBase = LOWER_OFFSET

		p = ord(char) - txtBase
		k = ord(key[index]) - keyBase
		nChar = 0
		if encrypt:
			nChar = (p + k) % TOTAL_CHAR
		else:
			nChar = (p - k) % TOTAL_CHAR

		totalStr += chr(nChar + txtBase)

		index += 1
		if index >= len(key):
			index = 0
	
	return totalStr

def affineCipher(aOffset, bOffset, plain_text, encrypt):
	global UPPER_OFFSET, LOWER_OFFSET, TOTAL_CHAR

	totalStr = ""

	for char in plain_text:
		if char == " ":
			totalStr += " "
			continue
		if not char.isalpha():
			totalStr += char
			continue

		base = UPPER_OFFSET
		if not char.isupper():
			base = LOWER_OFFSET

		offset = 0
		charIndex = ord(char) - base
		if encrypt:
			offset = (aOffset * charIndex) + bOffset
		else:
			aOffset = pow(aOffset, -1, TOTAL_CHAR) # Inverse A
			offset = aOffset * (charIndex - bOffset)

		offset = offset % TOTAL_CHAR

		totalStr += chr(offset + base)
	
	return totalStr

while loop:
	clear()

	cipher = None

	print(ASCII_TEXT)
	print(random.choice(splash))

	print()
	print("-1 -> Exit")
	print(" 1 -> Vigenère Cipher")
	print(" 2 -> Affine Cipher")

	while True:
		try:
			cipher = int(input("What Cipher would you like to do? "))
		except:
			print("Input valid choice.")
			continue
		
		match cipher:
			case -1:
				exit()
			case 1:
				break
			case 2:
				break
			case _:
				print("Input valid choice.")

	
	totalStr = ""
	encrypt  = True

	while True:
		choice = input("Encrypt? (Y/N) ").lower()

		if choice != "y" and choice != "n":
			print("Input valid choice.")
		else:
			encrypt = choice == "y"
			break

	match cipher:
		case 1:
			plain_text = input("Input Text: ")
			key        = input("Input Key:  ")
			
			totalStr = vigenereCipher(plain_text, key, encrypt)
		case 2:
			plain_text = input("Input Text: ")

			aOffset = 0
			bOffset = 0
			while True:
				try:
					aOffset = int(input("Input A Offset: "))
					bOffset = int(input("Input B Offset: "))

					break
				except:
					print("Input valid offset.")

			totalStr = affineCipher(aOffset, bOffset, plain_text, encrypt)

	print(totalStr)
	input("Press enter to continue.")