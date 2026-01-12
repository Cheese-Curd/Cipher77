import importlib.util
import random
import os
import importlib

import TerminalHelper as terminal

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

def errPrint(*args):
	print(f"{terminal.Text.Colors.RED}{" ".join(map(str, args))}{terminal.Text.RESET}")

while loop:
	clear()

	cipher = None

	print(f"{terminal.Text.Styles.BOLD}{terminal.Text.Colors.LIGHT_PURPLE}{ASCII_TEXT}{terminal.Text.RESET}")
	print(f"{terminal.Text.Styles.ITALIC}{random.choice(splashes)}")

	print()
	errPrint(f"-1 -> Exit {terminal.Text.Styles.ITALIC}(Exit the Program)")

	for i, cipher in enumerate(ciphers, start=1):
		print(f"{terminal.Text.Colors.BLUE} {i} -> {cipher.name} {terminal.Text.Styles.ITALIC}({cipher.desc}){terminal.Text.RESET}")

	while True:
		try:
			cipher = int(input("What Cipher would you like to do? "))
		except:
			errPrint("Input valid choice.")
			continue
		
		if cipher == -1:
			clear()
			print("Goodbye!")
			exit()
		
		if 0 <= (cipher - 1) < len(ciphers):
			break
		else:
			errPrint("Input valid choice.")
	
	totalStr = ""
	encode  = True

	while True:
		choice = input("Encode? (Y/N): ").lower()

		if choice != "y" and choice != "n":
			errPrint("Input valid choice.")
		else:
			encode = choice == "y"
			break

	plain_text = input("Input Text: ")
	totalStr = ciphers[cipher - 1].cipher(plain_text, encode)

	if totalStr == None:
		errPrint("ERR: Cipher does not have an output!")
	else:
		print(f"{terminal.Text.Colors.LIGHT_GREEN}Result:\n\t{totalStr}{terminal.Text.RESET}")

	input("Press enter to continue.")