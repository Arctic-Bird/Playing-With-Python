print("Hello world!")

def multiply():
    while True:
        try: # You can have some input validation in your 'Hello World' program, as a treat.
            input1 = int(input("Enter an integer: "))
            input2 = int(input("Enter ANOTHER integer: "))
            product = input1 * input2
            print(product)
        except ValueError:
            print("Hey DUMBASS! I asked you to enter INTEGERS!") # It loops until you enter an integer :) Someone buffer overflow this mf
            continue
        else:
            break

multiply()