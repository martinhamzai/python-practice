'''
Random password generator in Python taking in inputs from the user
and utilizing the secrets module for security.
'''

import secrets

uc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
      'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
      'Y', 'Z']

lc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
      'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
      'y', 'z']

nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

syms = ['`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

def main():
    print("Password Generator\n")
    while True:
        try:
            length = int(input("Enter the desired length: "))
            print()
            break
        except:
            print("Invalid length")

    chars = []

    # get options
    while True:
        upper = input("Use uppercase letters? (y or n): ")
        if upper == 'y':
            chars.extend(uc)
            break
        elif upper == 'n':
            break

    while True:
        lower = input("Use lowercase letters? (y or n): ")
        if lower == 'y':
            chars.extend(lc)
            break
        elif lower == 'n':
            break

    while True:
        numbers = input("Use numbers? (y or n): ")
        if numbers == 'y':
            chars.extend(nums)
            break
        elif numbers == 'n':
            break

    while True:
        symbols = input("Use symbols? (y or n): ")
        if symbols == 'y':
            chars.extend(syms)
            break
        elif symbols == 'n':
            break

    if len(chars) == 0:
        print("\nMust select at least one type of character.")
        return

    password = ""

    for i in range(length):
        password += chars[secrets.randbelow(len(chars))]

    print(f"\nPassword: {password}")


if __name__ == "__main__":
    main()