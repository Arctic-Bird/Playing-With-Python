def fizzBuzz():
    for integer in range(1, 101):
        if integer % 15 == 0:
            print("FizzBuzz")
        elif integer % 5 == 0: # Elif must always come after an if statement!
            print("Buzz")
        elif integer % 3 == 0:
            print("Fizz")
        else: # The else statement after if and elif statements is optional
            print(integer)
        
    return integer

print(fizzBuzz())

'''If the first if statement checks if integer % 3 is 0, 
then it'll apply to the integer % 15 == 0 statement as well. So, check if integer % 15 is 0 FIRST!
After that, the elif statements can be in either order. I just did it descending because it looks nicer.
'''

# Single line if statement:
num = 6
fizz = 'Fizz' if num % 3 == 0 else n # This is similar to list and dictionary comprehensions!