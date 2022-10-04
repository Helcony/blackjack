import random
from replit import clear
print('''
          _____                              88          88                       88        ""                       88 
         |A .  | _____                       88          88                       88                                 88       
         | /.\ ||A ^  | _____                88,dPPYba,  88 ,adPPYYba,  ,adPPYba, 88   ,d8  88 ,adPPYYba,  ,adPPYba, 88   ,d8  
         |(_._)|| / \ ||A _  | _____         88P'    "8a 88 ""     `Y8 a8"     "" 88 ,a8"   88 ""     `Y8 a8"     "" 88 ,a8"  
         |  |  || \ / || ( ) ||A_ _ |        88       d8 88 ,adPPPPP88 8b         8888[     88 ,adPPPPP88 8b         8888[  
         |____V||  .  ||(_'_)||( v )|        88b,   ,a8" 88 88,    ,88 "8a,   ,aa 88`"Yba,  88 88,    ,88 "8a,   ,aa 88`"Yba,  
                |____V||  |  || \ / |        8Y"Ybbd8"'  88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a 88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a     
                       |____V||  .  |                                                      ,88    
                              |____V|                                                    888P"  
''')
start = input('Would you like to start playing? ').lower

def list_sum(cards):
    return cards[0] + cards[1]

def main():
    user_cards = [random.randint(1, 13), random.randint(1, 13)]
    comp_cards = [random.randint(1, 13), random.randint(1, 13)]
    print(f'Your cards: {user_cards}')
    print(f"Computer's first card: {comp_cards[0]}")
    decide = input("'y' to get another card, 'n' to pass: ").lower()
    if decide == 'yes' or 'y':
        if sum(user_cards) > sum(comp_cards):
            print(f'Your final hand: {user_cards}')
            print(f"Computer's final hand: {comp_cards}")
            print('You win!! ')
        elif sum(user_cards) == sum(comp_cards):
            print(f'Your final hand: {user_cards}')
            print(f"Computer's final hand: {comp_cards}")
            print('It is a tie!! ')
        else:
            print(f'Your final hand: {user_cards}')
            print(f"Computer's final hand: {comp_cards}")
            print('You lose!! ')

        play_again = input('Would you like to play again? ').lower()
        if play_again == 'yes' or play_again == 'y':
            print('wtf')

        elif play_again == 'no' or play_again == 'n':
            print('Thanks for playing! ㋡')
            exit()
    if decide == 'no' or 'n':
        exit()


if start == 'yes' or 'y':
    main()
else:
    exit()
