lista = []
with open("input.txt") as f:
    for line in f:
        lista.append(line.strip())
suurin = 0
idlist = []
for sana in lista:
    rivi = sana[:7]
    sarake = sana[-3:]
    rivi = rivi.replace("F", "0").replace("B", "1")
    sarake = sarake.replace("R", "1").replace("L", "0")
    rivi = int(rivi, 2)
    sarake = int(sarake, 2)
    seatid = rivi*8 + sarake
    if seatid > suurin:
        suurin = seatid
    idlist.append(seatid)
res = [ele for ele in range(max(idlist) + 1) if ele not in idlist]
print(res)
