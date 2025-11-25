x = None
while type(x) != int:
    x = int(input('how many bytes: '))

# if x // 10 < 100:
#     print(x, 'bytes')
# elif x // 10 < 100_000:
#     print(x // 1000, 'kilobytes')
# elif x // 10 < 100_000_000:
#     print(x // 1000000, 'megabytes')
# elif x // 10 < 100_000_000_000:
#     print(x, 'gigabytes')
# elif x // 10 < 100_000_000_000_000:
#     print(x // 1000000000, 'terabytes')
# else:
#     print('more than terabytes not supported')

#----------------------------------------------------------------------
# count = 0
# units = ['bytes', 'KB', 'MB', 'GB', 'TB']
#
# while x >= 1000 :
#     x = x / 10
#     count += 1
#     print(x)
# unit_index = count // 3
#
# print(int(x), units[unit_index])

#---------------------------------more than TB-------------------------------------
count = 0
n = 0
units = ['bytes', 'KB', 'MB', 'GB', 'TB']

while n < len(units) :
    x = x / 1000
    count += 1
    n += 1
    print(x)
unit_index = count

print(int(x), units[unit_index-1])
