def move_player(x, y, direction, turns_allowed, player_speed):

    if direction == 0 and turns_allowed[0]:  # Right
        x += player_speed
    elif direction == 1 and turns_allowed[1]:  # Left
        x -= player_speed
    elif direction == 2 and turns_allowed[2]:  # Up
        y -= player_speed
    elif direction == 3 and turns_allowed[3]:  # Down
        y += player_speed

    return x, y
