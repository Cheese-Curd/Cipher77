UPPER_OFFSET = 65
LOWER_OFFSET = 97
TOTAL_CHAR   = 26TOTAL_CHAR   = 26

def getOffset(char):
	base = UPPER_OFFSET
	if not char.isupper():
		base = LOWER_OFFSET

	return base
