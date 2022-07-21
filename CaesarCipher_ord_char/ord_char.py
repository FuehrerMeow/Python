
phrase = "hello world"

encryption = ""
for char in phrase:
    if char.islower():
        unicode_char = ord(char)
        new_unicode_char = unicode_char + 3
        new_char = chr(new_unicode_char)
        encryption += new_char
    else:
        encryption += char
print(encryption)
