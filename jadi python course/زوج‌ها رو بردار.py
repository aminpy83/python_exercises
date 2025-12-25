def pick_evens(*args):
    list =[]
    for i in range(len(args)):
        if args[i] %2 ==0:
            list.append(args[i])
    return list
    

x = map( int, input().split())
print(pick_evens(*x))