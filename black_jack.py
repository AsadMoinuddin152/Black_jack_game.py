############### Blackjack Project #####################

import random

def deal_card():
  """Its give a random card as the output which can be stored in the variable."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

###############   ###############
def calculate_score(cards):
  """This function calculates the total score and give the score as the output and replace the ace with 1 if the score is crossing 21 when the ace is in
"""
  
  if sum(cards) == 21 and len(cards) == 2:
    return 0

  
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)
###############   ###############

def compare_score(user_score, computer_score):
  if user_score == computer_score:
    return "Draw 😜😜"
  elif computer_score == 0:
    return "Lose, The opponent has Black Jack 😱😱😱"
  elif user_score == 0:
    return "Won, You have the Black Jack 😎😎😎"
  elif user_score > 21:
    return "You have went over 21.\nYou lose."
  elif computer_score > 21:
    return "Opponent went over 21.\nYou won"
  elif user_score > computer_score:
    return "You won."
  else:
    return "You lose."

###############   ###############
def play_game():
  user_cards = []
  computer_cards = []
  is_game_over = False
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  
  while not is_game_over:
  
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your cards :  {user_cards} and Current score : {user_score}")
    print(f"Computer First card : {computer_cards[0]}")
    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      user_should_deal = input("Do you want to draw another card. Type 'y' for draw a card or 'n' to pass : ")
      if user_should_deal == "y":
        user_cards.append(deal_card())
      else:
        is_game_over = True
  
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
  
  
  print(f"Your Final hand is {user_cards} and Final Score is {user_score}")
  
  print(f"Oponnent Final hand is {computer_cards} and Final Score is {computer_score}")
  print(compare_score(user_score, computer_score))
###############   ###############   ###############
#Main code which will be excuted first
while input("Do you want to play Black Jack Game. Type 'y' for yes and 'n' for no : ") == 'y':
  play_game()
