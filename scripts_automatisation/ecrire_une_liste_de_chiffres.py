f = open("nombres.txt", "w")

for i in range(1,11):
    f.write(f"{str(i)}\n")

f.close()