from datetime import datetime

current_time_plus_five = (datetime.now().second + 5) % 60 # 60 seconds in a minute. Basic time!
def wait_until_future(time):
    while datetime.now().second != time: # Wait five seconds to print the output
        pass # "Move along." Great as a placeholder!
    print(f'The current time is {time} seconds after the {datetime.now().minute}th minute of the hour')


wait_until_future(current_time_plus_five)

def breakStatement(time):
    while True:
        if datetime.now().second == time:
            print(f'The current time is {time} seconds after the {datetime.now().minute}th minute of the hour')
            break # Break out of the current loop it's in, or the FIRST loop it's in if you're using nested loops

breakStatement(current_time_plus_five)

def continueStatement(time):
    while True:
        if datetime.now().second < time:
            continue # Keep going until the if clause is no longer correct
        break # Get out of the while loop after the if clause isn't true anymore!
    print(f'The current time is {time} seconds after the {datetime.now().minute}th minute of the hour')

continueStatement(current_time_plus_five)


# Begin for loop practice

my_list = [1, 2, 3, 4]
for item in my_list:
    print(item) # Very basic loop that prints each value in a list

animalLookup = {
    'a': ['aardvark', 'antelope', 'ant'],
    'b': ['bear', 'bumblebee'],
    'c': ['cat'],
}

for letter, animals in animalLookup.items(): # Only prints when it finds a list with only one value
    if len(animals) > 1:
        continue
    print(f"Only one animal in list(s) {letter}")

for letter, animals in animalLookup.items():
    if len(animals) > 1:
        print(f'Found {len(animals)} animals in list {letter}')
        break # Breaks as soon as the if statement is met. Although list "b" contains more than 1 animal, list "a" already satisfies this.


# Begin for/else practice

# Find primes from 2 to 100:
for number in range(2, 100):
    for factor in range(2, int(number**0.5) + 1):
        if number % factor == 0:
            break # Done. If the remainder is 0, the number is even and is therefore NOT prime
    else:
        print(f'{number} is prime')


# break/else can also be used in a while loop