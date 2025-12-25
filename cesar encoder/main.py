l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
     'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

text = input("Word: ")
x = input("encode or decode? ").lower()
shift = int(input("how many shifted to right? "))


def encode(t, s):
    t = list(t)
    final = ""
    for i in range(len(t)):
        for j in l:
            if t[i] == j :
                index = l.index(j) + shift
                if index >= 26:
                    index -= 26  
                final += l[index]  
    print(final)

def decode(t, s):
    t = list(t)
    final = ""
    for i in range(len(t)):
        for j in l:
            if t[i] == j :
                index = l.index(j) - shift
                if index >= 26:
                    index = index % 26  
                final += l[index]  
    print(final)

if x == "encode":
    encode(text, shift)
elif x == "decode":
    decode(text, shift)
else:
    print("i did't undrestand your demand!", x)

