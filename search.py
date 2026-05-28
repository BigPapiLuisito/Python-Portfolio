#search.py
#luis s.
#Generate a random secret number between 1 and 100.

import random
def linear_search():
    secret_number = random.randint(1,100)
    print(f"The secret number is: {secret_number}")
    guess = 0
    attempt = 0
    print("Starting Linear Search...")
    for guess in range(1,101):
        if guess != secret_number:
            print("Uh oh... that is wrong, try again.")
            attempt += 1
            continue
        else:
            print("Congrats on finding the secret number!")
            break
    print(f"Congrats! It took you {attempt} attempts!")


def binary_search():
    secret_number = random.randint(1,100)
    print(f"The secret number is: {secret_number}")
    attempt = 0
    low = 1
    high = 100
    found = False
    print("Starting binary search...")
    while not found:
        attempt += 1
        mid = (low + high)//2
        if mid < secret_number:
            low = mid + 1
        elif mid > secret_number:
            high = mid - 1
        else:
            print("Congratulation! You got the secret number!")
            found = True
    print(f"It took about {attempt} attempts!")

binary_search()
