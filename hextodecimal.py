hexnumbers = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6':6, '7':7,
    '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}

def hexToDec(num): # Simpler to understand, but lots of unnecessary writing. You don't need all these if-elif-else statements! A loop works fine!

    for char in num:
        if char not in hexnumbers:
            print(f'{char} is not a hex character!')
            return None

    if len(num) > 3 or len(num) == 0: # Problem specifically says your hex number cannot be above three digits
        return None
    elif len(num) == 3:
        return (hexnumbers[num[0]] * 256) + (hexnumbers[num[1]] * 16) + (hexnumbers[num[2]])
    elif len(num) == 2:
        return (hexnumbers[num[0]] * 16) + (hexnumbers[num[1]])
    else:
        return (hexnumbers[num[0]])


def hexToDecLoop(num): # Probably the better way of approaching this problem. Included for my own learning purposes.
    for char in num:
        if char not in hexnumbers:
            return None # Can't give you an answer if a value you passed isn't a hexadecimal value! The example given in the course I'm taking is 'Z.' Z is not a hexadecimal value.

    converted = 0
    exponent = len(num) - 1
    for char in num:
        converted = converted + (hexnumbers[char] * (16 ** exponent)) # I was adding hexnumbers[char] and 16^whatever instead of multiplying them like an IDIOT
        exponent = exponent - 1
    return converted

initialNumber = 'A'
print(hexToDec(initialNumber))
print(hexToDecLoop(initialNumber))