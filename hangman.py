import random

def hangman():
    # List of words to choose from
    words = ["python", "hangman", "programming", "computer", "algorithm"]
    word = random.choice(words)  # Randomly choose a word from the list
    guessed_word = ["_"] * len(word)  # Create a list to store the correctly guessed letters
    guessed_letters = set()  # Set to store the letters that have already been guessed
    attempts = 6  # Number of wrong attempts allowed

    print("Welcome to Hangman!")
    print(" ".join(guessed_word))  # Show the initial empty word with underscores

    while attempts > 0:
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print(f"You've already guessed '{guess}'. Try a different letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed_word[i] = guess
            print("Good guess!")
        else:
            attempts -= 1
            print(f"Wrong guess! You have {attempts} attempts left.")

        print(" ".join(guessed_word))  # Show the current state of the word

        if "_" not in guessed_word:
            print("Congratulations! You've won!")
            break
    else:
        print(f"Sorry, you've lost. The word was '{word}'.")

if __name__ == "__main__":
    hangman()
