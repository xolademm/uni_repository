import random

def print_hangman(tries):
    stages = [
        """
           -----
           |   |
               |
               |
               |
               |
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        """,
        """
           -----
           |   |
           O   |
          /|\  |
               |
               |
        """,
        """
           -----
           |   |
           O   |
          /|\  |
          /    |
               |
        """,
        """
           -----
           |   |
           O   |
          /|\  |
          / \  |
               |
        """
    ]
    print(stages[6 - tries])

def print_board(word, guessed_letters):
    display_word = ' '.join([letter if letter in guessed_letters else '_' for letter in word])
    print(display_word)

def hangman():
    words = ['python', 'java', 'ruby', 'javascript']
    word = random.choice(words)
    guessed_letters = set()
    tries = 6

    while tries > 0:
        print_hangman(tries)
        print_board(word, guessed_letters)

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess not in word:
            tries -= 1
            print(f"Wrong guess. You have {tries} tries left.")

        if all(letter in guessed_letters for letter in word):
            print("Congratulations! You've guessed the word.")
            print_board(word, guessed_letters)
            break
    else:
        print_hangman(tries)
        print(f"Sorry, you've lost. The word was '{word}'.")

if __name__ == "__main__":
    hangman()
