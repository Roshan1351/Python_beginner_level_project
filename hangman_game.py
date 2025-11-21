import random

def hangman():
    words = ["python", "code", "alpha", "program", "developer"]
    word = random.choice(words)
    guessed = []
    tries = 6

    print("🎮 Welcome to Hangman!")
    print("_ " * len(word))

    while tries > 0:
        guess = input("Guess a letter: ").lower()

        if guess in guessed:
            print("You already guessed that!")
            continue

        guessed.append(guess)

        if guess in word:
            print("Good guess!")
        else:
            tries -= 1
            print(f"Wrong guess! {tries} tries left.")

        display = [letter if letter in guessed else "_" for letter in word]
        print(" ".join(display))

        if "_" not in display:
            print("You win! The word was:", word)
            return

    print("💀 Game over! The word was:", word)

if __name__ == "__main__":
    hangman()