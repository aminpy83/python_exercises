def sum_numbers(*args):

    if not args: 
        return 0
   
    return sum(args)

x = map( int, input().split())
print(sum_numbers(*x))