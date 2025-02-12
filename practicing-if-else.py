def fizzBuzz():
    for integer in range(1, 101):
        if integer % 15 == 0:
            print("FizzBuzz")
        elif integer % 5 == 0:
            print("Buzz")
        elif integer % 3 == 0:
            print("Fizz")
        else:
            print(integer)
        
    return integer

print(fizzBuzz())

'''If the first if statement checks if integer % 3 is 0, 
then it'll apply to the integer % 15 == 0 statement as well. So, check if integer % 15 is 0 FIRST!
After that, the elif statements can be in either order. I just did it descending because it looks nicer.
'''