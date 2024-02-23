redtext = "GGG Man ^I am delighted?"

for i in range(0, len(redtext)):
    if redtext[i].isalnum() == False:
        redtext = redtext[0:i] + "f"+redtext[i+1:]
print(redtext)
