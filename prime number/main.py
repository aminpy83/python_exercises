from math import ceil
number = int(input("give me a number: "))
def is_prime(a):
    n = ceil(number/2)
    flag = True
    for i in range(n+1, 2, -1):
        if number % i == 0 :
            print("not a prime number", i)
            flag = False
            break
    if (flag):
        print("you send a prime number")
is_prime(number)