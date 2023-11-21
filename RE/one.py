import re
str = input("Enter String:")
matcher = re.finditer('[ab]', str)

for match in matcher:
    print(match.start(), '....', match.end(), '....'+match.group())
