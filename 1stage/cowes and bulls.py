import random

rand_number = []
round = 0

def random_number():
    while len(rand_number) < 4:
        r = random.randint(0,9)
        if r not in rand_number:
            rand_number.append(r)
    return(rand_number)


##tarberakner voronq chen ahsxatum
    # for i in range(4):
        # r = random.randint(0,9)
        # for l in rand_number:
        #     if r == l:
        #         rand_number.clear()
        #         random_number()
        #     else:
        #         rand_number.append(r)



    # if len(rand_number) != len(set(rand_number)):
    #     rand_number.clear()
    #     random_number()
    # else:
    #     rand_number.append(r)

def game():
    global round
    round += 1
    cows = 0
    bulls = 0
    guess_number = input("guess the number")
    guess = []

    for i in range(4):
        guess.append(int(guess_number[i]))
    for x in range(4):
        for y in range(4):
            if (guess[x] == rand_number[y]):
                cows += 1
    for j in range(4):
        if guess[x] == rand_number:
            bulls += 1


    print("bulls",bulls)
    print("cows",cows)
    print("rounds", round)
    if round != 4:
        game()

    user_check = input("do you wanna play again, print yes\n")
    if user_check == "yes":
        game()
    else:
        print("yeee")    

random_number()
game()
