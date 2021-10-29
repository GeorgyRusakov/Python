v=[1]
for num in range(50):
    v.append(num)
mod=v[0]
for num in v:
    if num > mod and num % 2 == 0:
        mod=num
print(mod)
