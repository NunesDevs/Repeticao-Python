l1 = int(input("Digite o numero da piramide: "))
for l2 in range(0, l1):
    for l3 in range(0, l1 - l2 - 1):
        print(end=" ")
    for l3 in range(0, l2 + 1):
        print("*", end= ' ')
    print()
