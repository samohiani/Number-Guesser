#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
from art import logo
print(logo)

def difficulty():
  level = input("Choose a diificulty, EASY or HARD: ").lower()
  if level == "easy":
    return 10
  elif level == "hard":
    return 5
  else:
    return "Invalid Input"
 
def check_guess(guess, number, lives):
  """Checks answer against guess. Return number of lives left"""
  if (guess == number) and (lives == (5 or 10)):
    print("That was Quick, Good Job😎")
  elif guess == number:
    print(f"You guessed the number with {lives} lives left.😤")
  elif guess < number:
    print("Too low")
    return lives - 1
  elif guess > number:
    print("Too high")
    return lives - 1
      
def play_game():
  print("Welcome to Number Guesser!")
  print("I'm thinking of a number between 1 and 100")
  answer = random.choice(range(1,101))
  print(answer)
  lives = difficulty()
  user_guess = 0
  while user_guess != answer:
    print(f"You have {lives} attempts to guess the number")
    user_guess = int(input("Guess a number: "))
    lives = check_guess(user_guess, answer, lives)
    if lives == 0:
      print("You've run out of lives, you lose.\nThanks for playing🤪")
      return

play_game()