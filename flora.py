import random


def number_validation (number):
    pass
    # its not a number
    # return False

    # its not within range
    # return false

    # return True

def check(rand, user_n):
    if rand == user_n:
        return "SAME"
    elif rand > user_n:
        return "HIGHER"
    elif rand < user_n:
        return "LOWER"


def test_check():
    my_rand = 10
    user_n= 10
    exp_res = "SAME"

    test_res = check(my_rand, user_n)

    assert exp_res == test_res
    assert exp_res is str


def get_inp():
    return input("GIVE ME: ")

def main():
    lives = 5
    rnd_num = random.randrange(1,20)

    user_num = input("GIVE ME: ")
    valid = number_validation(user_num)

    if valid:
        res = check(rnd_num, int(user_num))


main()