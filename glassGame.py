move, movement =  input().split()
move, movement = int(move), str(movement)


def glass_game(movement, move):
    # get multiple input
    for i in range(1, move + 1):
        #split input
        first, second = map(str, input().split())
    # find goal
        if movement == second :
            movement = first
        elif movement == first :
            movement = second
    return movement

print(glass_game(movement, move))
    

