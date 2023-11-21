import re
matcher = re.finditer("a{2}", "ababaabaaaaba")
#                              012345678910

for match in matcher:
    print(match.start(), '....', match.group())
