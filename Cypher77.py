import importlib.util
import random
import os
import importlib

ASCII_TEXT = r"""
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
    os.system("cls" if os.name == "nt" else "clear")

def loadCiphers():
	ciphers = []

	for filename in os.listdir("ciphers"):
		if not filename.endswith(".py") or filename.startswith("_"):
			continue

		path = os.path.join("ciphers", filename)
		name = filename[:-3]

		spec = importlib.util.spec_from_file_location(name, path)
		cipher = importlib.util.module_from_spec(spec)
		spec.loader.exec_module(cipher)

		# Make sure it's actually a cipher module
		if not all(hasattr(cipher, attr) for attr in ("name", "desc", "cipher")):
			continue

		ciphers.append(cipher)

	# Return sorted list of ciphers so it stays consistent
	return sorted(ciphers, key=lambda c: c.name.lower())

ciphers = loadCiphers()

# plain_text = input("Input Text: ")
# for i, cipher in enumerate(ciphers, start=1):
# 	print(f"{i} -> {cipher.name}")
# 	print(f"\t{cipher.desc}")

# 	print(cipher.cipher(plain_text))

while loop:
	clear()

	cipher = None

	print(ASCII_TEXT)
	print(random.choice(splashes))

	print()
	print("-1 -> Exit (Exit the Program)")

	for i, cipher in enumerate(ciphers, start=1):
		print(f" {i} -> {cipher.name} ({cipher.desc})")

	while True:
		try:
			cipher = int(input("What Cipher would you like to do? "))
		except:
			print("Input valid choice.")
			continue
		
		if cipher == -1:
			exit()
		
		if 0 <= (cipher - 1) < len(ciphers):
			break
		else:
			print("Input valid choice.")
	
	totalStr = ""
	encode  = True

	while True:
		choice = input("Encode? (Y/N): ").lower()

		if choice != "y" and choice != "n":
			print("Input valid choice.")
		else:
			encode = choice == "y"
			break

	plain_text = input("Input Text: ")
	totalStr = ciphers[cipher - 1].cipher(plain_text, encode)

	if totalStr == None:
		print("ERR: Cipher does not have an output!")
	else:
		print(totalStr)

	input("Press enter to continue.")