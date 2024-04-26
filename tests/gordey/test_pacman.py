from game_module import Ghost

def test_ghost_movement():
    player_position = (5, 5)
    ghost = Ghost("Blinky", "normal", (3, 3))

    # Move towards player
    assert ghost.move(player_position) == (4, 4), \
        "Ghost should move towards the player"

    # Change mode to frightened and test movement away from the player
    ghost.mode = "frightened"
    assert ghost.move(player_position) == (2, 2), \
        "Ghost should move away from the player"

    # Change mode to scatter and test random movement
    ghost.mode = "scatter"
    initial_position = ghost.position
    new_position = ghost.move(player_position)
    assert new_position != initial_position, \
        "Ghost should move randomly"