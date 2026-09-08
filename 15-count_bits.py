n = int(input('enter num,ber: '))
count = 0
while n > 0:
    if n & 1:
        count = count + 1
        n = n >> 1
print("number of bit sets ", count)