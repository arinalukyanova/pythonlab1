name = input("Имя: ").split()
s = 0
for i in name:
    s += len(i)
print("Инициалы:",f"{name[0][0]}{name[1][0]}{name[2][0]}",".") 
print("Длина (символов):",s+2)