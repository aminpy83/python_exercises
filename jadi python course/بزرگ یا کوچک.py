def is_greater(a, b):
    if a > b:
        return True
    return False

a, b  = map(int , input().split())
print(is_greater(a,b))