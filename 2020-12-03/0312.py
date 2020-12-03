def laskin(alas, sivulle):
    with open("input.txt") as f:
        input = f.read()
        input = input.strip().split("\n")
        j = 0
        xcounter = 0
        input = input[int(alas)::int(alas)]
        for rivi in input:
            j += sivulle
            jmodulo = j % len(i)
            if(rivi[jmodulo] == "#"):
                xcounter += 1
    return xcounter

def main():
    print(laskin(1,1)*laskin(1,3)*laskin(1,5)*laskin(1,7)*laskin(2,1))
main()
