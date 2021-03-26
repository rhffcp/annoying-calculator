# Annoying Calculator

import random, time
import pyinputplus as pyip

def countdown(t):
    '''
    Countdown timer. Arguments passed into the function must be an integer representing seconds.
    '''

    while t:
        # divmod() displays the quotient and remainder after dividing its arguments.
        mins, secs = divmod(t, 60)
        # Because t is an input string, it must be converted to int using string formatting like below. 
        # (0=leading zero, 2=min width, d=integer)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        # end="\r" = carriage return - following line overwrites the previous line.
        print(timer, end="\r")
        time.sleep(1)
        # Decrement time until reaching 0.
        t -= 1

def mult_quiz():
    '''
    Multiplication quiz generator. The user is given three attempts and five seconds to solve each problem.
    '''

    total_problems = 10
    correct_answers = 0

    for problem in range(total_problems):
        # Pick two random numbers.
        num1 = random.randint(0,9)
        num2 = random.randint(0,9)
        prompt = f'{problem + 1}: {num1} x {num2} = '

        try:
            # The first arg in inputStr prints a prompt. The second arg contains a condition.
            # The ^ and $ characters in allowRegexes ensure that the answer begins and ends with the correct number.
            # The first argument in blockRegexes prevents every other possible string that doesn't match the correct answer.
            # The second argument prints 'Incorrect!' and restarts the question.
            pyip.inputStr(prompt, allowRegexes=[f'^{num1 * num2}$'], blockRegexes=[('.*', 'Incorrect!')], timeout=5, limit=3)
        # If the user answers after the 5 sec timeout has expired, a TimeoutException is raised.
        except pyip.TimeoutException:
            print('Out of time!')
        # If the user answers incorrectly more than 3 times, a RetryLimitException is raised.
        except pyip.RetryLimitException:
            print('Out of tries!')
        else:
            print('Correct')
            correct_answers += 1

    print('\nCalculating score...')
    time.sleep(1.5)
    print(f'\nScore: {correct_answers} / {total_problems}')
    time.sleep(1.5)
    print('Nice.')

def rock_paper_scissor():
    '''
    Rock, paper, scissor game. Wins, losses, and ties are recorded and displayed after each turn.
    '''

    # These variables keep track of the number of wins, losses, and ties.
    wins = 0
    losses = 0
    ties = 0

    # Game loop.
    while True:
        print(f'{wins} Wins, {losses} Losses, {ties} Ties')
        # Player input loop.
        while True:
            print('Enter your move: (r)ock (p)aper (s)cissors')
            player_move = input()
            if player_move == 'r' or player_move == 'p' or player_move == 's':
                break
            print('Invalid: you must type either r, p, or s')

        # Display what the player chose:
        if player_move == 'r':
            print('ROCK versus...')
            time.sleep(1)
        elif player_move == 'p':
            print('PAPER versus...')
            time.sleep(1)
        else:
            print('SCISSORS versus...')
            time.sleep(1)

        # Display what the computer chose:
        random_number = random.randint(1, 3)
        if random_number == 1:
            computer_move = 'r'
            print('ROCK')
        elif random_number == 2:
            computer_move = 'p'
            print('PAPER')
        else:
            computer_move = 's'
            print('SCISSORS')

        # Display and record the win/loss/tie.
        if player_move == computer_move:
            print("It's a tie!")
            ties += 1
        elif player_move == 'r' and computer_move == 's':
            print('You win!')
            wins += 1
        elif player_move == 'p' and computer_move == 'r':
            print('You win!')
            wins += 1
        elif player_move == 's' and computer_move == 'p':
            print('You win!')
            wins += 1
        elif player_move == 'r' and computer_move == 'p':
            print('You lose!')
            losses += 1
        elif player_move == 'p' and computer_move == 's':
            print('You lose!')
            losses += 1
        elif player_move == 's' and computer_move == 'r':
            print('You lose!')
            losses += 1

        if wins == 3:
            print("\nCongratulations! You've won!")
            break

# Main function.
def calculate(problems):
    '''
    This function solves simple arithmetic problems and returns the results in a vertically aligned format.
    However, the function comes with several annoying conditions:
    - to reveal the answer, the user must guess a specific number
    - once the user guesses the correct number, the user must solve a series of multiplication problems
    - once the user solves the problems, the user must defeat the computer in a game of rock, paper, scissors
    - once the user wins the game, the answers to the arithmetic problems will be revealed
    - operations must be formated as strings inside an array
    - operands are limited to 4 digits
    - the function can only solve up to 5 problems at a time
    '''

    # Number guessing game.
    win = False
    while win == False:
        secret_number = random.randint(1, 10)
        print("In order to reveal the answer, you must pass the number guessing game. Let's begin!")
        print('I am thinking of a number between 1 and 10.')

        # User gets 5 tries.
        for i in range(1, 6):
            guess = int(input('Take a guess: '))

            if guess < secret_number:
                print('Your guess is too low.')
            elif guess > secret_number:
                print('Your guess is too high.')
            else:
                break

        if guess == secret_number:
            print('\nGood job! You guessed my number in ' + str(i) + ' guesses!')
            win == True
            break
        else:
            print('Nope. The number I was thinking of was ' + str(secret_number) + '.')

    # Multiplication quiz.
    print('\nNext, you will need to solve a series of multiplication problems.')
    print("You'll be given three attempts and five seconds to solve each problem.")
    answer = input('Are you ready? yes or y\n').lower()

    if answer == 'yes' or answer == 'y':
        countdown(5)
        print('Begin!\n')
        time.sleep(1)
        mult_quiz()
    else:
        print('Too bad!')
        countdown(5)
        print('Begin!\n')
        time.sleep(1)
        mult_quiz()

    # Rock, paper, scissor.
    print('\nFinally, you must now play rock, paper, scissor with the computer and win three times. Only then will the answers be revealed.')
    answer = input('Are you ready? yes or y\n').lower()
    if answer == 'yes' or answer == 'y':
        countdown(5)
        print('Begin!\n')
        time.sleep(1)
        rock_paper_scissor()
    else:
        print('Too bad!')
        countdown(5)
        print('Begin!\n')
        time.sleep(1)
        rock_paper_scissor()

    # Evaluation and formatting.
    # Empty strings will be updated for final formatting.
    top = ''
    bottom = ''
    divider = ''
    operation_eval = ''

    # Limit number of problems to 5.
    if len(problems) > 5:
        return 'Error: Too many problems.'

    # Split each string into individual components.
    for problem in problems:
        problem = problem.split(' ')
        operand_left = problem[0]
        operator = problem[1]
        operand_right = problem[2]

        # Operator can only be + - * x and /.
        if operator != '+' and operator != '-' and operator != '*' and operator != 'x' and operator != '/':
            return "Error: Invalid operation symbol."

        # Operands can only contain digits.
        if operand_left.isalpha() or operand_right.isalpha():
            return 'Error: Operands must only contain digits.'

        # Limit operands to 4 digits.
        if len(operand_left) > 4 or len(operand_right) > 4:
            return 'Error: Operands are limited to 4 digits.'

        # Evaluation of operation + removal of trailing zeros.
        if operator == '+':
            evaluation = str(float(operand_left) + float(operand_right)).rstrip('0').rstrip('.')
        elif operator == '-':
            evaluation = str(float(operand_left) - float(operand_right)).rstrip('0').rstrip('.')
        elif operator == '*' or operator == 'x':
            evaluation = str(float(operand_left) * float(operand_right)).rstrip('0').rstrip('.')
        else:
            evaluation = str(float(operand_left) / float(operand_right)).rstrip('0').rstrip('.')

        # Right-align operands and place the operator on the same line as the second operand.
        top_length = len(operand_left) + len(operand_right) + len(operator)
        bottom_length = len(operand_left) + len(operand_right)
        top_align = operand_left.rjust(top_length)
        bottom_align = operator + operand_right.rjust(bottom_length)

        # Dashes will run along the entire length of each problem.
        dashes = ''
        for i in range(top_length):
            dashes += '-'

        # Right-aligned operands, dashes, and operation evaluations assigned to empty string variables.
        # Add 4 spaces to each so that there are 4 spaces between each problem.
        top += top_align + '    '
        bottom += bottom_align + '    '
        divider += dashes + '    '
        operation_eval += evaluation.rjust(top_length) + '    '

    # Formatted answers.
    time.sleep(1.5)
    print("\nGreat work! In 30 seconds, the answers will be revealed. You deserve it!")
    time.sleep(1.5)
    countdown(30)
    return top + '\n' + bottom + '\n' + divider + '\n' + operation_eval


# Example
print(calculate(['122 x 2', '1.2 + 2', '2.2 * 2', '5 / 2']))


