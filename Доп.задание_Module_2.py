def numbers(num):
    
    password = []
   
    for a in range(1, 21):
        for b in range(1, 21):
            if num % (a + b) == 0:
                password.append(f"{a}{b}")
   
    result = ''.join(password)
    return result
                
for num in range(3, 21):
   print(f"{num} - {numbers(num)}")