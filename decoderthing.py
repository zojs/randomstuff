noter=input("Tekst: ")
ven=""
for c in noter:
    if chr(ord('a')+4)<=c<=chr(ord('v')+4) or chr(ord('A')+4)<=c<=chr(ord('V')+4):
        ven+=chr(ord(c)-4)
    elif chr(ord('w')-22)<=c<=chr(ord('z')-22) or chr(ord('W')-22)<=c<=chr(ord('Z')-22):
        ven+=chr(ord(c)+22)
    else:
        ven+=c
print(ven)
