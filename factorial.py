print("Witness my attempts to program a couple of factorial functions!")

fact_input = int(input("Enter an integer: ")) # Takes an integer as user input... is it even possible to calculate the factorial of a floating point number?

def calculate_factorial(n):
    if n == 0:
        return 1 # The factorial of 0 and 1 is 1! (not a terrible math joke. Write that down.)
    else:
        return calculate_factorial(n - 1) * n # Factorials are calculated like this: n = n * (n - 1) * (n - 1) * (n - 1)... until "n" reaches 1 (see comment on line 7). This is a recursive implementation.

def factorial_loop(n): # This one required some more thinking on my part, due to me being godawful with loops and programming in general.

    """ 
    Variable "result" is set to 1, and is multiplied by itself and n with each loop. n is decremented by 1 with each loop. Say n = 5. The loop *should* go like this:

    1 = 1 * 5
    5 = 5 * 4
    20 = 20 * 3
    60 = 60 * 2
    120 = 120 * 1 < This is 5!
    """

    result_question_mark = 1
    while n > 1: # See comments on lines 7 and 9.
        result_question_mark = result_question_mark * n 
        n = n - 1
    print(result_question_mark)

maybe_the_answer = calculate_factorial(fact_input)
print(maybe_the_answer)

factorial_loop(fact_input)