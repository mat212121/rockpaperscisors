import random
from game import choices
computer = random.choice(choices)
player = None
while player not in choices:
  player = input("rock, paper, or scissors?: ").lower()

from game import game
game()
print("computer:",computer)
print("player:",player)

