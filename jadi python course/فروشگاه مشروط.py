price = int(input())
if 20000 <= price <= 50000 :
    price = price - (price/10)

elif 50000 < price :
    price = price - 2*(price/10)


print(int(price))