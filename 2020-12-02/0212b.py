laskuri = int(0)
with open("input.txt") as f:
    for line in f:
        line = line.strip().split()
        paikat = line[0].split("-")
        kirjain = line[1][0]
        sana = line[2]
        paikka1 = int(paikat[0])-int(1)
        paikka2 = int(paikat[1])-int(1)
        if((sana[paikka1] == kirjain) ^ (sana[paikka2] == kirjain)):
            laskuri += 1
    print(laskuri)
