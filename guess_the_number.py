import random

lvl_num = 20
attempts = 0
lives = 5
lvl = 0

''' 
Function generates a random random based on the on the range from 1 to 20
Depending on the level the range decreases by half every level
In addition the function also includes a variable that counts the number
the player can attempt to guess the number before losing
'''
def randomizer(lvl_num, lives):
    if lvl == 0:
        pass
    elif lvl == 1:
        lvl_num //= 2
        lives -= 2
        print(f"Level: {lvl}! \nYou have {lives} lives for this level!")
    else:
        lvl_num //= 4
        lives -= 3
        print(f"Level: {lvl}! \nYou have {lives} lives for this level!")
    usr_num = input(f"Guess the number from range 1 to {lvl_num}: ")
    valid_num = catch_me(usr_num)
    check_output = check_input(valid_num, lvl_num)
    rnd_num = random.randrange(1,lvl_num)
    return rnd_num, check_output, lives
   
'''
Function verifiying if the user input is valid
based on if the number is not outside the number range of the level
''' 
def check_input(usr_num, lvl_num):
    if usr_num <= lvl_num:
        return usr_num
    else:
        usr_input = input(f"Number is outside of range, enter a number between 1 and {lvl_num}: ")
        chk_sum = catch_me(usr_input)
        usr_num = check_input(chk_sum,lvl_num)
    return usr_num

'''
Function that verifies that the player input is an integer
'''
def catch_me(usr_input):
    while usr_input:
        try:
            if int(usr_input):
                return int(usr_input)
        except ValueError:
            chk_input = input(f"The input is not a number, type a number from 1 to {lvl_num}: ")
            usr_num = catch_me(chk_input)
        return usr_num
    
'''
The main function of the guessing game, the results from the randomizer function are loaded to the
the guess_the_number and split into variables for comparison to the number generated
'''
def guess_the_number(randomizer):
    attempts = 0
    usr_num = randomizer[1]
    rnd_num = randomizer[0]
    lives = randomizer[2]
    while randomizer:
        if usr_num == rnd_num:
            attempts += 1
            print(f"You guessed right, the number is: {usr_num}! \nAttempts: {attempts}!")
            break
        else:
            attempts += 1
            if lives - 1 == 0:
                exit("You run out of lives!")
            else:
                lives -= 1
                print(f"Lives left: {lives}")
                if usr_num > rnd_num:
                    usr_input = input("The number is lower. Try again: ")
                    
                else:
                    usr_input = input("The number is higher. Try again: ")
                
                chk_num = catch_me(usr_input)
                usr_num = check_input(chk_num, lvl_num)

''' 
Starts the game!
'''                          
def complete_all_levels():
    global lvl
    while lvl < 3:
        guess_the_number(randomizer(lvl_num, lives))
        lvl += 1
        if lvl == 3:
            y_or_n = input("Would you like to play again! \nPress Yes(y) to 'continue' or No(n) to 'exit': ")
            if y_or_n.lower() == "y":
                lvl = 0
                complete_all_levels()
            else:
                exit("Max level complete! \nYou have completed the game!")
    

complete_all_levels()