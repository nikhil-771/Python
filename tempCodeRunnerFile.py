#prime number
num = 100
l=[2]
for i in range(2, 100):
    flag = 1
    for j in l:
        if i%j == 0:
            flag = 0
            break
    if flag:
        l.append(i)
print(l)