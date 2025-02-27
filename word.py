import random
a=str(input("enter your name:"))
print(f"welcome {a}")
print("lets play a game")
# List of words and their descriptions
word_descriptions = {
     'nebula': 'A giant cloud of dust and gas in space, often a birthplace for stars.',
    'alchemy': 'An ancient practice that combined science, philosophy, and mysticism to transform matter.',
    'labyrinth': 'A complex and confusing network of passages or paths, often used metaphorically.',
    'zenith': 'The highest point or peak, often used to describe success or celestial objects.',
    'mirage': 'An optical illusion caused by atmospheric conditions, making distant objects appear displaced.',
    'serendipity': 'An unexpected and fortunate discovery that happens by chance.',
    'quasar': 'A highly energetic celestial object at the center of a galaxy, powered by a black hole.',
    'epiphany': 'A sudden realization or insight, often leading to a deeper understanding.',
    'cryptic': 'Mysterious or difficult to understand, often used to describe puzzles or messages.',
    'paradox': 'A statement or situation that contradicts itself but may still hold truth.',
    'cascade': 'A small waterfall or a process where events happen in rapid succession.',
    'horizon': 'The apparent line where the earth meets the sky, symbolizing limits or new beginnings.',
    'eclipse': 'An astronomical event where one celestial body blocks the light of another.',
    'chimera': 'A mythical creature composed of parts from different animals; also used for unrealistic dreams.',
    'reverie': 'A state of being lost in a pleasant daydream or deep thought.',
}

# Randomly selecting a word
word = random.choice(list(word_descriptions.keys()))
description = word_descriptions[word]

# Displaying the description
print("\nHint: " + description)
print("Guess the characters!")
guesses = ''
turns = 12
while turns>0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char)
        else:
            print("_")
            failed += 1
    if failed == 0:
        print("You Win")
        print("The word is: ", word)
        break
    guess = input("guess a character:")
    guesses += guess
    if guess not in word:
        turns -= 1
        print("Wrong")
        print("You have", + turns, 'more guesses')
        if turns == 0:
            print("You Loose")
print("thank you for playing")            