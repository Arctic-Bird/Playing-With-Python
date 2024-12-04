print("Hello world!")

def multiply():
    while True:
        try:
            input1 = int(input("Enter an integer: "))
            input2 = int(input("Enter ANOTHER integer: "))
            product = input1 * input2
            print(product)
        except ValueError:
            print("Hey DUMBASS! I asked you to enter INTEGERS!")
            continue
        else:
            break

multiply()