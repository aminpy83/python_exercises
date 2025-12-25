def skyline(*args):
    if not args or len(args) <1 :
        return 0
    return max(args)



x = map( int, input().split())
print(skyline(*x))