def isValidInput(binary_string):
    # Remove underscores
    binary_string = binary_string.replace("_", "")
    # Check if the binary string only contains '0' and '1'
    return all(char in '01' for char in binary_string)

def bin2dec(binary_string):
    # Remove underscores
    binary_string = binary_string.replace("_", "")
    decimal_value = 0
    power = len(binary_string) - 1

    # Convert binary to decimal
    for char in binary_string:
        if char == '1':
            decimal_value += (2 ** power)
        power -= 1

    return decimal_value

def main():
    while True:
        binary_string = input("Enter a binary number: ")

        # Check if the input is valid
        if isValidInput(binary_string):
            decimal_output = bin2dec(binary_string)
            print(f"Decimal value: {decimal_output}")
        else:
            print("Invalid binary number. Please enter a string of '0,' '1,' and '_' only.")

main()