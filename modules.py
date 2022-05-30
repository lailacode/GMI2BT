from random import randint  

def number_list(num_one, num_two):                          # input från användaren i parameterlistan
    num_list = []                                           # skapa lista
    for num in range(1, 1000):                              # for loop för nummer mellan 1 och 1000
        if num % num_one == 0 and num % num_two == 0:       # om num är delbart med input från användren
            num_list.append(num)                            # läggs till i listan
    print(num_list)                                         # listan skrivs ut
    print()                                                 # mellanrum
    
def guess_number():
    guess_list = 0                                                             # variabel för antal gissningar
    number = randint(1, 100)                                                   # ett tal slumpas ut
    guess = int(input('Guess a number from 1 to 100. \n'))                     # låta användaren gissa
    
    while (guess_list != number):                                              # så länge gissningarna inte är lika med rätt nummer körs loopen
        if guess < number:
            guess = int(input('Your guess is too low. Try again. \n'))         # berättar för användaren om gissningen är för låg
            
        elif guess > number:
            guess = int(input('Your guess is too high. Try again. \n'))        # berättar för användaren om gissningen är för hög
            
        else:
            print('Good job! You guessed right!')                              # berättar för användaren att de gissat rätt
            print('The right number is: %d' %(number))
            break                                                              # avbryta loopen