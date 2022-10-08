def prime_checker(number):
    a=0
    divisors=[]  
    for i in range(1,number+1):
        if(number%i==0):
            divisors.append(i)
            a+=1
    if(a==2):
        print(f"It's a prime number. {divisors}")
    else:
        print(f"It's not a prime number.{divisors}")        
'''
def prime_checker(number):
    is_prime=True
    for i in range(2,number):       
        if number%i==0:
            is_prime=False
    if is_prime:
        print("It's a prime number.")        
    else:
        print("It's not a prime number.")
'''  
n = int(input("Check this number: "))
prime_checker(number=n)