def octal_to_binary(octal):
    # Converting Octal to Decimal
    decimal = 0
    power = 0
    while octal != 0:
        decimal += (octal % 10) * pow(8, power)
        octal //= 10
        power += 1
 
    # Converting Decimal to Binary
    binary = 0
    digit_place = 1
    while decimal != 0:
        binary += (decimal % 2) * digit_place
        decimal //= 2
        digit_place *= 10
 
    return binary
 
# Sample Input
octal_number = int(input())
 
# Octal to Binary Conversion
binary_number = octal_to_binary(octal_number)
 
# Output
print(binary_number)