from random import randint

options = ['sang', 'kaghaz', 'gheichi']
scores = {'player':0, 'computer':0}
round_number = 1
rounds = 0
player_choice = None
pc_choice = None

while rounds < 1 :
    rounds = int(input("How many rounds do you want to play? "))
    while round_number <= rounds:
        if rounds - round_number == 0:
            print(10 * '-', 'Final Match', 10 * '-')
        else:
            print('round number',round_number)

        round_number += 1
        pc_choice = options[randint(0,2)]
        player_choice = input(f'choose sth( {options[0]}, {options[1]}, {options[2]}): ').lower()

        if player_choice not in options:
            print('Invalid choice, please try again')
            while player_choice not in options:
                player_choice = input(f'choose sth( {options[0]}, {options[1]}, {options[2]}): ')

        if player_choice == pc_choice:
            print(f'your choice: {player_choice}'
                  f' pc choice: {pc_choice} '
                  f'Draw!')

        elif player_choice == options[0] and pc_choice == options[1]:
            scores['computer'] += 1
            print(f'winner: pc,  pc choice: {pc_choice}, score: {scores.items()}')
        elif player_choice == options[0] and pc_choice == options[2]:
            scores['player'] += 1
            print(f'winner: you,  pc choice: {pc_choice}, score: {scores.items()}')

        elif player_choice == options[1] and pc_choice == options[2]:
            scores['computer'] += 1
            print(f'winner: pc,  pc choice: {pc_choice}, score: {scores.items()}')
        elif player_choice == options[1] and pc_choice == options[0]:
            scores['player'] += 1
            print(f'winner: you,  pc choice: {pc_choice}, score: {scores.items()}')

        elif player_choice == options[2] and pc_choice == options[0]:
            scores['computer'] += 1
            print(f'winner: pc,  pc choice: {pc_choice}, score: {scores.items()}')
        elif player_choice == options[2] and pc_choice == options[1]:
            scores['player'] += 1
            print(f'winner: you,  pc choice: {pc_choice}, score: {scores.items()}')

    if scores['player'] > scores['computer']:
        print('You win!', scores)
    elif scores['player'] < scores['computer']:
        print('You lose!', scores)
    else:
        print('Draw!')