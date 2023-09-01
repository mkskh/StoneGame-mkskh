print('Welcome to the Stone Game! \n')

count = int(input('Please write the total number of stones in the pile: '))
max_num = int(input('Please write the maximum number of stones that can be taken at ones: '))
name1 = input('Please enter the name of Player 1: ')
name2 = input('Please enter the name of Player 2: ')
turn = int(input('Enter the player number who will start the game (1 or2): '))

print('\n The Game Starts!')

while count > 0:
    print('\n Current stone count:', count)
    cur_player = name1 if turn == 1 else name2
    take = int(input(f"{cur_player}'s turn. Enter a number of stone to take(1-{max_num}): "))
    
    if take < 0 or take > max_num or take == None:
        print('Invalid number. Please try again.')
        continue

    count -= min(take, count)
        

    # if cur_player == name1:
    #     turn = 2
    # elif cur_player == name2:
    #     turn = 1

    turn = 2 if cur_player == name1 else 1 

    print(f'The winner is {cur_player}')




