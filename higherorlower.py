from random import randrange

number = randrange(1, 11)

while True:
    print(number)
    try:
        guess = float(input("Your guess?"))
    except NameError:
        print("Not a number try again")
        continue
    if guess > number:
        print("it's smaller")
    elif guess < number:
        print("it's larger")
    else:
        print("it's correct!")
        break
