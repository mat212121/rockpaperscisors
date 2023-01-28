import random
while True:
  choices = ["rock","paper","scissors"]

  computer = random.choice(choices)
  player = None

  while player not in choices:
    player = input("rock, paper, or scissors?: ").lower()

  print("computer:",computer)
  print("player:",player)

  def lose():
    print("You lose!")

  def win():
    print("You Win!")

  def game():
    if player == computer:
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
  game()
  play_again = input("Play again? (yes/no): ").lower()
  if play_again != "yes":
    break
print("Bye")
