import random


def values(min,max): #function for choosing a random integer for the question
    """
    Random integer.
    """
    #return random.uniform(min,max)
    return random.randint(int(min), int(max)) #returns a random integer within the range 


def operation():
    '''function to choose which mathematical operation to perform'''

    return random.choice(['+', '-', '*']) #randomly chooses a symbol from the given options


def result(n1, n2, o):  
    '''function to calculate the actual answer'''
    p = f"{n1} {o} {n2}" #formatting the question with the symbol and random numbers
    
    '''for choosing the operation to perform'''
    if o == '+': a = n1 + n2 
    elif o == '-': a = n1 - n2
    else: a = n1 * n2
    return p, a

def math_quiz():
    s = 0
    total =5
    #t_q = 3.14159265359

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for turn in range(total):
        n1 = values(1, 10); n2 = values(1, 5.5); o = operation() 

        PROBLEM, ANSWER = result(n1, n2, o)
        print(f"\nQuestion: {PROBLEM}")
        try:
            useranswer = input("Your answer: ")
            useranswer = int(useranswer)
        except: 
            print("well that's not a number, moving on.....")
            continue

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            s += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {s}/{total}")

if __name__ == "__main__":
    math_quiz()
