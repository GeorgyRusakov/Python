v=[1]
for num in range(40):
    v.append(num)
mod=[]
for num in v:
    if num % 2 == 0 and num < 10:
        mod.append(num)
if len(mod) == 0:
    print("Не подходит условию")
else:
    print(mod)
