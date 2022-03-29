import random

# Constant for the possible colors
colors = "YORPGB"

# Create a secret - a 4-letter word using the possible colors (with duplicates allowed)
secret = "YORP"   # just an example

# Start the game
round = 1
print(f"Round {round}")

# Get a valid guess from the input
guess = "ORRR"    # just an example

# The message if the input is not a valid guess:
# print(" Please write 4-letter words using the characters Y, O, R, P, G, B!")

# Inspect the guess, calculate HITS and CLOSE
hits = 1          # for the R at position 3
close = 1         # for the O at position 1
print(f"Hits: {hits} Close: {close}\n")


# The message if the game is won:
# print(f"Congratulations, you broke the code! The secret was {secret}.")

print(f"You have run out of attempts, you lost the game. The secret was {secret}.")
