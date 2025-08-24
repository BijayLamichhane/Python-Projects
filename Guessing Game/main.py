import random

easy_words = ['apple', 'train', 'tiger', 'monkey']
medium_words = ['python', 'bottle', 'caterpillar']
hard_words = ['umbrella', 'mow', 'silicon']

print("Welcome to the guessing game 🎉")
print('Choose a difficulty level: easy, medium, hard')

level = input("Enter a difficulty: ").lower()

if level == 'easy':
    secret = random.choice(easy_words)
    max_attempts = 10
elif level == 'medium':
    secret = random.choice(medium_words)
    max_attempts = 7
elif level == 'hard':
    secret = random.choice(hard_words)
    max_attempts = 5
else:
    print("Invalid choice. Defaulting to easy level")
    secret = random.choice(easy_words)
    max_attempts = 10

attempts = 0
print(f"\nGuess the word! It has {len(secret)} letters.")

while attempts < max_attempts:
    guess = input("Enter your guess: ").lower()
    attempts += 1

    if guess == secret:
        print(f'🎉 Congratulations! You guessed it in {attempts} attempt(s).')
        break

    # Create hint
    hint = ''.join([guess[i] if i < len(secret) and guess[i] == secret[i] else '_' for i in range(len(secret))])
    print("Hint: " + hint)
    print(f"Attempts left: {max_attempts - attempts}\n")

else:
    print(f"😢 Out of attempts! The word was '{secret}'.")

print("Game Over")
