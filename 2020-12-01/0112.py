expenses = []
with open('input.txt') as f:
    for line in f:
        expenses.append((line.strip()))

for i in expenses:
    for j in expenses:
        for k in expenses:
            if(int(i) + int(j) + int(k) == 2020):
                print(i, j, k, int(i)*int(j)*int(k))
