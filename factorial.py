print("Witness my attempts to program a factorial function!")

fact_input = int(input("Enter an integer: "))

def calculate_factorial(n):
    if n == 0:
        return 1
    else:
        return calculate_factorial(n - 1) * n

def factorial_loop(n2):
    result_question_mark = 1
    while n2 > 1:
        result_question_mark = result_question_mark * (n2)
        n2 = n2 - 1
    print(result_question_mark)

maybe_the_answer = calculate_factorial(fact_input)
print(maybe_the_answer)

factorial_loop(fact_input)