"""
write a program that uses a generator that generates characters from string in reverse order
"""
s = "ahem"
reverse = (n for n in s[::-1])
for value in reverse:
    print(value)