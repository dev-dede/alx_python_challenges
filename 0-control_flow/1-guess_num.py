import random
secret_number = random.randint(1, 10)
guess = int(input("I'm thinking of a number between 1 and 10. Can you guess it? "))

match guess:
    case _ if guess == secret_number:
        print("Congratulations, you guessed it!")
    case _:
        print("Nope")
print(secret_number)