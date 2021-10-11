decimal = int(input("Enter decimal value: "))
octal = oct(decimal).replace("0o", "")

print(f"Octal value of {decimal} is {octal}")