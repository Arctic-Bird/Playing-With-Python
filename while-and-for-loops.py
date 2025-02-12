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