KEFALAIA = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLM"
MIKRA = "abcdefghijklmnopqrstuvwxyzabcdefghijklm"
rot13 = ""

keimeno = input ("Grapste to keimeno sas edw: ")

for i in keimeno:
    if i in KEFALAIA:
        rot13 = rot13 + KEFALAIA[KEFALAIA.find(i) + 13]
    elif i in MIKRA:
        rot13 = rot13 + MIKRA[MIKRA.find(i) + 13]
    else :
        rot13 = rot13 + i

print(rot13)