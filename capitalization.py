from cs50 import get_string

s = get_string("Word: ")

for c in s:
    print(c.upper(), end="")

print()