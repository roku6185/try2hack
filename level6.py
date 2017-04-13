#!/usr/bin/python

# (USERNAME)
username = ["aaabb", "aaaaa", "aaaab", "abbab", "ababb", "aaaab"]

# (PASSWORD)
password = ["aabaa", "abbaa", "aaaba", "baaaa", "babba", "abbba", "baaba", "abaaa", "abbab", "abbaa", "baaaa", "aaaaa", "babaa", "abaab", "baaab"]

# (PAGE)
page = ["babab", "aabab", "abaab", "abbab", "aabbb", "aaaba"]

# Baconian chipher
baconian = {"AAAAA": "a", "AABBA": "g", "ABBAA": "n", "BAABA": "t", "AAAAB": "b", "AABBB": "h", "ABBAB": "o", "BAABB": "u", "BAABB": "v", "AAABA": "c", "ABAAA": "i", "ABAAA": "j", "ABBBA": "p", "BABAA": "w", "AAABB": "d", "ABAAB": "k", "ABBBB": "q", "BABAB": "x", "AABAA": "e", "ABABA": "l", "BAAAA": "r", "BABBA": "y", "AABAB": "f", "ABABB": "m", "BAAAB": "s", "BABBB": "z"}

# Decipher text segments
output_str = ""

for chunk in username:
	output_str += baconian[str(chunk).upper()]
output_str += " "

for chunk in password:
	output_str += baconian[str(chunk).upper()]
output_str += " "

for chunk in page:
	output_str += baconian[str(chunk).upper()]
output_str += " "

print output_str
