while(True):
    num = input("Number: ")
    if (num != "Exit"):
        st = int(input("Enter system type of number (10, 2, 8, 16): "))
        dec = int(num, st)
        print(f"Bin: {bin(dec).replace('0b', '')}\nDec: {dec}\nOct: {oct(dec).replace('0o', '')}\nHex: {hex(dec).replace('0x','').upper()}")
    else:
        break