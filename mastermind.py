import random

# Constant for the possible colors
colors = "YORPGB"
n = random.randint(0, 5)
random_letter = colors[n]

# Create a secret - a 4-letter word using the possible colors (with duplicates allowed)
# secret = "YORP"   # just an example
secret = ""
for i in range(4):
    n = random.randint(0, 5)
    secret += colors[n]

History = []
# Start the game
round = 1
while round <= 12:
    print("Round " +  str(round))
    guess_is_invalid = True 
    while guess_is_invalid:
        guess = raw_input("Enter your guess: ").upper()
        if len(guess) == 4:
            guess_is_invalid = False
            for letter in guess:
                if letter not in colors:
                    guess_is_invalid = True
            if guess_is_invalid:
                print(" Please write 4-letter words using the characters Y, O, R, P, G, B!")
    hits = 0
    for i in range(4):
        if guess[i] == secret[i]:
            hits += 1          
    close = 0
    for color in colors:
        close += min(secret.count(color), guess.count(color))
    close = close - hits         
    print("Hits: " + str(hits)+ " Close: " + str(close))
    if hits == 4:
        break
    History.append((guess, hits, close))
    round += 1
if hits == 4:
    print("Congratulations, you broke the code! The secret was " + str(secret) + ".")
else:
    print("You have run out of attempts, you lost the game. The secret was " + str(secret) + ".")
for row in History:
    print(" " + row[0] + " | " + str(row[1]) + " " + str(row[2]))



        
    
    


# Get a valid guess from the input
# guess = "ORRR"    # just an example


# The message if the input is not a valid guess:
# print(" Please write 4-letter words using the characters Y, O, R, P, G, B!")

# Inspect the guess, calculate HITS and CLOSE



# The message if the game is won:
# print(f"Congratulations, you broke the code! The secret was {secret}.")

# print(f"You have run out of attempts, you lost the game. The secret was {secret}.")
