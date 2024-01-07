logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

print(logo)
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
draw = "y"
#Card Chooser
player_cards = random.sample(cards, 2)
bot_cards = random.sample(cards, 2)
#Bot card fixer
while sum(bot_cards) < 17:
  bot_cards.append(random.sample(cards, 1)[0])
  
play = input("Do you want to play blackjack? (y for yes and n for no)\n")

if play.lower() == "y":
  print(f"Your cards are {player_cards} and your total points are {sum(player_cards)}")
  print(f"One of your dealers card is {bot_cards[1]}")
  draw = input("Do you want to draw a card? (y for yes, n for no) \n")
  if draw.lower() == "y":
    while draw.lower() == "y":
      player_cards.append(random.sample(cards, 1)[0])
      if sum(player_cards)>21:
        print(f"Your cards are {player_cards} and your total points are {sum(player_cards)}")
        print("Your points went over 21, you lose :(")
        exit()
      print(f"Your cards are {player_cards} and your total points are {sum(player_cards)}")
      draw = input("Do you want to draw a card? (y for yes, n for no) \n")


  final_player_points = sum(player_cards)
  final_bot_points = sum(bot_cards)
  print(f"Your cards are {player_cards} and your total points are {sum(player_cards)}")
  print(f"The bots cards are {bot_cards} and their total points are {sum(bot_cards)}")
  if final_bot_points > 21:
    print("You win, the bots points went over 21 :)")
  if final_bot_points > final_player_points:
    print("The bot wins, he has more points than you :(")
  elif final_bot_points < final_player_points:
    print("You win, you have more points than the bot :)")
  else:
    print("The game was a draw!")
  
  
else:
    print("Goodbye!")
