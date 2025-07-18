import random
word_list = ["apple", "python", "hangman", "coding", "game"]
word = random.choice(word_list).lower()
guessed_letters = []
max_attempts = 6
attempts_left = max_attempts
print("🎮 Welcome to Hangman!")
print("Guess the word, one letter at a time.")
print("_ " * len(word))  
while attempts_left > 0:
    guess = input("\nEnter a letter: ").lower()
    if not guess.isalpha() or len(guess) != 1:
        print("❗ Please enter a single alphabetic character.")
        continue
    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
        continue
    guessed_letters.append(guess)
    if guess in word:
        print("✅ Correct!")
    else:
        attempts_left -= 1
        print(f"❌ Incorrect! Attempts left: {attempts_left}")
    display = [letter if letter in guessed_letters else "_" for letter in word]
    print("Word:", " ".join(display))
    if "_" not in display:
        print("\n🎉 Congratulations! You guessed the word:", word)
        break
else:
    print("\n💀 Game Over! The correct word was:", word)
