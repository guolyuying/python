secret_word = "goomba"
guess = "" # You can leave this value blank like this "", or put in any random value (e.g. "pizza", 2, True) that's not gonna affect the following code.

while guess != secret_word:
    guess = input("Guess a creature name: ")
print("You got it! It's the Gooooooomba!")

# -----------------------------------------------

secret_word = "goomba"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Guess a creature name: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("You're out of guesses :(")
else:
    print("You got it! It's the Gooooooomba!")