n = int(input())
x = int(input())

n += 1

for _ in range(1,n) :
    if x % 2 == 1 :
        x = (x *2) -1
    else :
        x = (x /2)

print(int(x))