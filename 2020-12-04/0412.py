import re

def lista_splitter(lista, erotin):
    group = []
    for x in lista:
        if x != erotin:
            group.append(x)
        elif group:
            yield group
            group = []

def filtteri():
    lista = []
    with open("input.txt") as f:
        for lines in f:
            asd = lines.strip().split(" ")
            if(asd != ''):
                lista = lista + asd
            else:
                lista = []
    validit = []
    separator = ''
    lista = list(list_splitter(lista, separator))
    for alkio in lista:
        if([s for s in alkio if("eyr") in s] and [s for s in alkio if("hgt") in s] and [s for s in alkio if("byr") in s] and [s for s in alkio if("iyr") in s] and [s for s in alkio if("hcl") in s] and [s for s in alkio if("ecl") in s] and [s for s in alkio if("pid") in s]): # hyi saatana
            validit.append(alkio)
    return validit

def main():
    validit = filtteri()
    lopulliset = 0
    for alkio in validit:
        for sisalto in alkio:
            sisalto = sisalto.split(":")
            if sisalto[0] == "byr":
                if(int(sisalto[1]) >= 1920 and int(sisalto[1]) <= 2002):
                    ehto += 1
            elif sisalto[0] == "iyr":
                if(int(sisalto[1]) >= 2010 and int(sisalto[1]) <= 2020):
                    ehto += 1
            elif sisalto[0] == "eyr":
                if(int(sisalto[1]) >= 2020 and int(sisalto[1]) <= 2030):
                    ehto += 1
            elif sisalto[0] == "hgt":
                lukuosa = int(''.join(list(filter(str.isdigit, sisalto[1])))) # ei näin
                if(sisalto[1][-2:] == "cm" and (lukuosa >= 150 and lukuosa <= 193)):
                    ehto += 1
                elif(sisalto[1][-2:] == "in" and (lukuosa >= 59 and lukuosa <= 76)):
                    ehto += 1
            elif sisalto[0] == "hcl":
                pattern = re.compile("#[a-f0-9]{6}")
                if(pattern.fullmatch(sisalto[1])):
                    ehto += 1
            elif sisalto[0] == "ecl":
                if(sisalto[1] == "amb" or sisalto[1] == "blu" or sisalto[1] == "brn" or sisalto[1] == "gry" or sisalto[1] == "grn" or sisalto[1] == "hzl" or sisalto[1] == "oth"):
                    ehto += 1
            elif sisalto[0] == "pid":
                pattern = re.compile("[0-9]{9}")
                if(pattern.fullmatch(sisalto[1])):
                    ehto += 1
        if(ehto == 7):
            lopulliset += 1

main()
