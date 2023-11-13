import random

lvl = 0
range_num = 20

def input_num():
    global range_num
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
            if 0 < int(usr_input) < range_num:
                return int(usr_input)
            else:
                usr_input = input(f"Number is outside of range, enter a number between 1 and {range_num}: ")
                
        except ValueError:
            usr_input = input(f"The input is not a number, type a number from 1 to {range_num}: ")
            
def check_in(range_num, rnd_num, attempts, lvl, lives):
    usr_input = input_num()    
    for turns in range(lives):
        if lives > 1:
            usr_input = catch_me(usr_input, range_num)
            if rnd_num == usr_input:
                    attempts += 1
                    print(f"You guessed right, the number is: {usr_input}! \nAttempts: {attempts}!")
                    return True
            elif rnd_num > usr_input:
                attempts += 1
                lives -= 1
                print(f"Lives left: {lives}")
                usr_input = input("The number is higher. Try again: ")    
            elif rnd_num < usr_input:
                attempts += 1
                lives -= 1
                print(f"Lives left: {lives}")
                usr_input = input("The number is lower. Try again: ") 
        else:
            exit("You run out of lives!")

def die_repeat(lvl):
    if lvl == 3:
        y_or_n = input("Would you like to play again! \nPress Yes(y) to 'continue' or No(n) to 'exit': ")
        if y_or_n.lower() == "y":
            lvl = 0
            complete_all_levels()
        else:
            exit("Max level complete! \nYou have completed the game!")
        

def complete_all_levels():
    """
    Starts the game!
    Function generates a random random based on the on the range from 1 to 20
    Depending on the level the range decreases by half every level
    In addition the function also includes a variable that counts the number
    the player can attempt to guess the number before losing
    """
    global lvl
    global range_num
    attempts = 0
    lives = 5
    rnd_num = random.randrange(1, range_num)
    while lvl < 3:
        if lvl == 0:
            pass
        elif lvl == 1:
            range_num //= 2
            lives -= 2
            print(f"Level: {lvl}! \nYou have {lives} lives for this level!")
        elif lvl == 2:
            range_num //= 2
            lives -= 3
            print(f"Level: {lvl}! \nYou have {lives} lives for this level!")
        else:
            die_repeat(lvl)
        
        status = check_in(range_num, rnd_num, attempts, lvl, lives)

        if status == True:
            lvl += 1
        
complete_all_levels()