laskuri = int(0)
with open("input.txt") as f:
    for line in f:
        line = line.strip().split()
        rajat = line[0].split("-")
        alaraja = rajat[0]
        ylaraja = rajat[1]
        kirjain = line[1][0]
        maara = line[2].count(kirjain)
        if(int(maara) >= int(alaraja) and int(maara) <= int(ylaraja)):
            laskuri += 1
    print(laskuri)
