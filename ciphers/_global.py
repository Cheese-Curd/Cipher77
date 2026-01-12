UPPER_OFFSET = 65
LOWER_OFFSET = 97
TOTAL_CHAR   = 26

def getOffset(char):
	base = UPPER_OFFSET
	if not char.isupper():
		base = LOWER_OFFSET

	return base

def getYesNo(inputText=""):
	while True:
		response = input(f"{inputText} (Y/N): ").lower()
		if response != "y" and response != "n":
			print("Input valid choice.")
		else:
			return response == "y"