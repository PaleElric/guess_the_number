import random

def input_num(range_num):
    usr_input = input(f"Guess the number from range 1 to {range_num}: ")
    return usr_input

def catch_me(usr_input,range_num):
    """
    Function that verifies that the player input is an integer
    Baased on the user input the function returns the user number 
    within the acceptable range number of the level, if false another
    input request is suggested that meets the requierements
    """
    while True:
        try:
            if 1 <= int(usr_input) <= range_num:
                return int(usr_input)
            else:
                usr_input = input(f"Number is outside of range, enter a number between 1 and {range_num}: ")
                
        except ValueError:
            usr_input = input(f"The input is not a number, type a number from 1 to {range_num}: ")
            
def check_in(range_num, usr_input, attempts, lives):
    """
    Main function of the script it takes the variables from
    previous function and appies it into a for loop until 
    the player guesses the correct number or they run out of lives
    """
    rnd_num = random.randint(1, range_num)
    count = 0
    for turns in range(lives):
        lives -= 1
        val_input = catch_me(usr_input, range_num)
        if rnd_num == val_input:
                attempts += 1
                print(f"You guessed right, the number is: {val_input}! \nAttempts: {attempts}!")
                return True
        elif rnd_num > val_input:
            if lives == 0:
                exit("You run out of lives!")
            else:
                usr_input = input("The number is higher. Try again: ")
                attempts += 1
                print(f"Lives left: {lives}")
        else:
            if lives == 0:
                exit("You run out of lives!")
            else:
                attempts += 1
                print(f"Lives left: {lives}")
                usr_input = input("The number is lower. Try again: ") 
    else:
        exit("You run out of lives!")
                        

def choices(lvl):
    """
    Simple function for the game to be reset or to exit 
    based on the users 'yes' or 'no' input
    """
    if lvl == 3:
        y_or_n = input("Would you like to play again! \nPress Yes(y) to 'continue' or No(n) to 'exit': ")
        if y_or_n.lower() == "y":
            complete_all_levels()
        else:
            exit("Max level complete! \nYou have completed the game!")
        

def complete_all_levels():
    """
    Starts the game!
    If the player guesses the number right the level progresses
    to the next one with a decrease in both range number and lives
    """
    lvl = 1
    attempts = 0
    while lvl <= 3:
        lives = 5
        range_num = 20
        if lvl == 0:
            pass
        elif lvl == 1:
            range_num //= 2
            lives -= 2
            print(f"Level: {lvl}! \nYou have {lives} lives for this level!")
        elif lvl == 2:
            range_num //= 4
            lives -= 3
            print(f"Level: {lvl}! \nYou have {lives} lives for this level!")
        else:
            choices(lvl)
        
        usr_input = input_num(range_num)
        status = check_in(range_num, usr_input, attempts, lives)

        if status == True:
            lvl += 1

def test_check():
    attempts = 0
    very_pseudo_rand = 1
    user_input = 1
    exp_res = True
    lives = 1

    test_res = check_in(very_pseudo_rand, user_input, attempts, lives)

    assert exp_res == test_res
    
        
complete_all_levels()
#test_check()