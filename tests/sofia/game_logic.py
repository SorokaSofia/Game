def move_player(x, y, direction, turns_allowed, player_speed):
    """
    Moves the player based on the given direction and allowed turns.

    Parameters:
        x (int): The current x-coordinate of the player.
        y (int): The current y-coordinate of the player.
        direction (int): The direction in which the player is moving.
                         0 - Right, 1 - Left, 2 - Up, 3 - Down
        turns_allowed (list of bool): A list indicating which directions are permissible.
                                      [right_allowed, left_allowed, up_allowed, down_allowed]
        player_speed (int): The speed at which the player moves.

    Returns:
        tuple: The new x and y coordinates of the player after movement.
    """
    if direction == 0 and turns_allowed[0]:  # Right
        x += player_speed
    elif direction == 1 and turns_allowed[1]:  # Left
        x -= player_speed
    elif direction == 2 and turns_allowed[2]:  # Up
        y -= player_speed
    elif direction == 3 and turns_allowed[3]:  # Down
        y += player_speed

    return x, y