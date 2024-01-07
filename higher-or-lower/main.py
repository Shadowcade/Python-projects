from game_data import data
from art import logo
from art import vs
import random
import os

print(logo)
correct = "true"
point = 0

#The funtion for clearing console
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

#Chossing infomation for Option A
def option_a():
  #Chooses random section for Option A
  random_section = random.choice(data)
  #Chooses name for Option A
  name = random_section['name']
  #Chooses follower count for Option A
  follower_count = random_section['follower_count']
  #Chooses description for Option A
  description = random_section['description']
  #Chooses country for Option A
  country = random_section['country']
  #Return all the infomation on Option A
  return name, description, country, follower_count

def option_b():
  #Chooses random section for Option B
  random_section = random.choice(data)
  #Chooses name for Option B
  name = random_section['name']
  #Chooses follower count for Option BA
  follower_count = random_section['follower_count']
  #Chooses description for Option B
  description = random_section['description']
  #Chooses country for Option B
  country = random_section['country']
  #Return all the infomation on Option B
  return name, description, country, follower_count

#Giving Option A a infomation as a list
a_data = option_a()

while correct == "true":
  #Chossing infomation for Option A
  b_data = option_b()

  #Declare who wins
  if a_data[3] > b_data[3]:
    win_decision = "a"
  else:
    win_decision = "b"

  #Ask for who they think has more followes
  print(f"Compare A: {a_data[0]}, a {a_data[1]}, from {a_data[2]}")
  print(vs)
  print(f"Against B: {b_data[0]}, a {b_data[1]}, from {b_data[2]}")
  answer = input("Who has more followers? Type 'A' or 'B': ").lower()

  #Chooses if they are right or wrong
  if answer == win_decision:
    clear_console()
    print(logo)
    point += 1
    print(f"You're right! Current score: {point}"	)
    a_data = b_data
  else:
    clear_console()
    correct = "false"

print(f"Sorry, that's wrong. Final score: {point}")
