# This is the word_guesser code.

import random # importing random for use

# Print the welcome
print("\nWelcome to the FILLQUEST game.\n")
print("Please Guess the word that fill the given blanks\n")
print("*** GAME RULE *** ")
print("You will have 6 lives. If you guessed one wrong letter you will lose 1 life.")

# random words in list
random_words = [
    "apple", "banana", "orange", "strawberry", "mango", "lemon",
    "car", "bicycle", "bus", "motorcycle", "airplane", "boat",
    "usa", "france", "japan", "australia", "brazil", "india",
    "emily", "daniel", "sophia", "liam", "olivia", "ethan",
    "pizza", "burger", "sushi", "pasta", "ice cream", "chocolate",
    "elephant", "lion", "giraffe", "dolphin", "kangaroo", "penguin"
]

# create some images by keywords for making game fun
lives = ['''
+---+
 |  |
 O  |
/|\ |
/ \ |
    |
======
''', '''
+---+
 |  |
 O  |
/|\ |
/   |
    |
======
''', '''
+---+
 |  |
 O  |
/|\ |
    |
======
''', '''
+---+
 |  |
 O  |
/ \ |
    |
======
''', '''
+---+
 |  |
 O  |
    |
    |
======
''', '''
+---+
 |  |
    |
    |
    |
======
''']

# Set a live for the player
set_of_lives = 5

# Randomly chose a word from the random_words 
random_word = random.choice(random_words)

# create a blanks as length of the random_word
blanks = []
for _ in range(len(random_word)):
    blanks += "_"

# put condition to take place if player have not guessed any and have
# more than 0 live 

while ("_" in blanks) and (set_of_lives > 0): 

    print(f"{' '.join(blanks)}") # combine the list in string 

    # display the player live in that image format
    a_life = lives[set_of_lives]
    print(a_life)

    # ask user to guess the letter
    user_letter = input("\nPlease guess a letter: ").lower()

    # give one condition if the user does not guess the correct letter
    if not user_letter in random_word:
        if set_of_lives == 0:
            print("\n Sorry you loose.")
            
        else:
            print(f"\nYou guessed {user_letter}, but not the right guess. You loose a life.\n")  
            set_of_lives = set_of_lives - 1 # decrease player life

    # else condition if the user guess the correct letter
    else:
        # Check the index where the letter is of the correct letter
        for index in range(len(random_word)):
            letter = random_word[index]
            if user_letter == letter:
                blanks[index] = letter # change the blanks by the user guessed letter if matched

if "_" not in blanks:
    print("\nYou won")

elif set_of_lives == 0:
    print("\nOOPS!! You finished your lives")
