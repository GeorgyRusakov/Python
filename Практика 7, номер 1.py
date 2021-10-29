def check(num): 
    kol = 0  
    for j in range(1, num):  
        if num % j == 0:  
            
            kol += 1  
    if kol > 2:  
        return False 
    else:  
        return True  


n = int(input('Введите натуральное число большее 2: '))  
for i in range(n, 2 * n):  
    if check(i) and check(i + 2):  
        print(f'{i} {i + 2}')  
