import random as rn



def get_choices():
  """Get choices for player and computer"""
  list = ['rock','paper','scissors']
  check = True
  def get_input(): # Create a get_input function
    player_choice = input('\nChoose your object\n(rock, paper or scissors):\n')
    return player_choice
  player_choice = get_input()  # Ask user for input
  while check:
    if player_choice not in list:
      print('Choose again')
      player_choice = get_input()
    else: 
      break
    
  computer_choice = rn.choice(list) # User andom module and choice method
  
  print(f'\nYou chose {player_choice}, Computer chose {computer_choice}\n')
  choices = {'player':player_choice, 'computer':computer_choice}
  return choices



score = {'player': 0, 
         'computer': 0}

def check_win(player,computer):
  if player == computer:
    print("It's A Tie!")
    score['player'] += 1
    score['computer'] += 1

  elif player == 'rock': 
    if computer == 'scissors':
      print('Player Wins! Rock smashes scissors!')
      score['player'] += 1
    else:
      print('Computer Wins')
      score['computer'] += 1

  elif player == 'paper':
    if computer == 'scissors':
      print("Computer Wins")
      score['computer'] += 1

    else:
      print('Player Wins')
      score['player'] += 1

  else:  #if scissors
    if computer == 'rock':
      print('Computer Wins! Rock smashes scissors!')
      score['computer'] += 1

    else:
      print('Player Wins! Scissors Cuts Paper!')
      score['player'] += 1
  

while 3 not in list(score.values()):
  choice = get_choices()
  check_win(list(choice.values())[0],list(choice.values())[1])

  print(f"\nYou score {score['player']} \nComputer score {score['computer']}")


