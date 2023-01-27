import random
choices = ["rock","paper","scissors"]
computer = random.choice(choices)
player = None
def lose():
  print("Computer:",computer)
  print("Player:",player)
  print("You lose!")
def win():
  print("Computer:",computer)
  print("Player:",player)
  print("You Win!")
def game():
  computer = random.choice(choices)
  player = None
  if player == computer:
      print("Computer:",computer)
      print("Player:",player)
      print("Tie!")
  elif player == "rock":
    if computer == "paper":
      lose()
    if computer == "scissors":
      win()
    elif player == "paper":
      if computer == "scissors":
        lose()
      if computer == "rock":
        win()
    elif player == "scissors":
      if computer == "rock":
        lose()
      if computer == "paper":
        win()
    
    