
h = int(input("height: "))

for i in range(1, h+1):
    p = "#" * i
    p = (" " * (h-i)) + p
    print(p)
