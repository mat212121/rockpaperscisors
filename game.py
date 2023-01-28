import random
def game():
  computer = random.choice(choices)
  player = None
  if player == computer:
      print("Computer:",computer)
      print("Player:",player)
      print("Tie!")
  elif player == "rock":
    if computer == "paper":
        print("Computer:",computer)
        print("Player:",player)
        print("You lose!")
    if computer == "scissors":
        print("Computer:",computer)
        print("Player:",player)
        print("You Win!")
    elif player == "paper":
      if computer == "sciss":
        print("Computer:",computer)
        print("Player:",player)
        print("You lose!")
      if computer == "rock":
        print("Computer:",computer)
        print("Player:",player)
        print("You Win!")
    
    