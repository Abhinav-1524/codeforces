n = int(input("enter length of square: "))
m = int(input("enter breadth of square: "))
a = int(input("flagstone :"))

flag_width= (n + a - 1) // a
flag_length = (m + a - 1) // a

flagstones = flag_width * flag_length

print(flagstones)
