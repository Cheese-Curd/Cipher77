import importlib.util
import random
import os
import importlib
import sys
import socket

import TerminalHelper as terminal

# Fixup file paths for when compiled
if getattr(sys, "frozen", False):
	base = os.path.dirname(sys.executable)
else:
	base = os.path.dirname(os.path.abspath(__file__))

if base not in sys.path:
	sys.path.insert(0, base)

ASCII_TEXT = r"""
 ██████╗██╗██████╗ ██╗  ██╗███████╗██████╗     ███████╗███████╗
██╔════╝██║██╔══██╗██║  ██║██╔════╝██╔══██╗    ╚════██║╚════██║
██║     ██║██████╔╝███████║█████╗  ██████╔╝        ██╔╝    ██╔╝
██║     ██║██╔═══╝ ██╔══██║██╔══╝  ██╔══██╗       ██╔╝    ██╔╝ 
╚██████╗██║██║     ██║  ██║███████╗██║  ██║       ██║     ██║  
 ╚═════╝╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝       ╚═╝     ╚═╝                                                        
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
		name = f"ciphers.{filename[:-3]}"

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

variables = {}

with open("variables.txt", "r", encoding="utf-8") as file:
	for line in file:
		line = line.strip()
		if not line or "=" not in line:
			continue

		key, value = line.split("=", 1)
		variables[key] = value.lower() == "true"

if variables["demo"] == True:
	clear()
	print("[ CIPHER 77 ]")
	print("Demo Mode Enabled. Press enter to continue.")
	input("")

baseTitle = "Cipher 77"
if variables["demo"]:
	baseTitle = "[DEMO] Cipher 77"

# Gets private IP
def getPIP():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	try:
		s.connect(('8.8.8.8', 80))
		IP = s.getsockname()[0]
	except Exception:
		IP = '127.0.0.1' # Fallback to localhost if no network connection
	finally:
		s.close()
	return IP

while loop:
	if variables["demo"]:
		terminal.setTitle(baseTitle)
	else:
		terminal.setTitle(baseTitle)
	clear()

	cipher = None

	if variables["title"] == True:
		print(f"{terminal.Text.Styles.BOLD}{terminal.Text.Colors.LIGHT_PURPLE}{ASCII_TEXT}{terminal.Text.RESET}")
	splash = random.choice(splashes)
	if splash == "I have your IP!!! 127.0.0.1!!!!":
		splash = f"I have your IP!!! {getPIP()}"
	
	print(f"{terminal.Text.Styles.ITALIC}{splash}")

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
			if variables["demo"] == True:
				print("[ CIPHER 77 ]")
				input("Thank you for viewing. Press enter to exit. ")
				clear()
			print("Goodbye!")
			terminal.exit(0)
		
		if 0 <= (cipher - 1) < len(ciphers):
			break
		else:
			errPrint("Input valid choice.")
	
	totalStr = ""
	encode  = True

	while True:
		terminal.setTitle(f"{baseTitle} - {ciphers[cipher - 1].name}")
		choice = input("Encode? (Y/N): ").lower()

		if choice != "y" and choice != "n":
			errPrint("Input valid choice.")
		else:
			encode = choice == "y"
			break

	plain_text = input("Input Text: ")
	totalStr = ciphers[cipher - 1].cipher(plain_text, encode, variables["demo"])

	if totalStr == None:
		errPrint("ERR: Cipher does not have an output!")
	else:
		print(f"{terminal.Text.Colors.LIGHT_GREEN}Result:\n\t{totalStr}{terminal.Text.RESET}")

	input("Press enter to continue.")