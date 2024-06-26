from random import randint


class Ghost:

    def __init__(self, name, mode, position):
        self.name = name
        self.mode = mode
        self.position = position

    def move(self, player_position):
        if self.mode == 'scatter':
            return self.move_randomly()
        if self.mode == 'frightened':
            return self.move_away_from(player_position)
        return self.move_towards(player_position)

    def move_randomly(self):
        self.position = (randint(0, 10), randint(0, 10))
        return self.position

    def move_towards(self, player_position):
        ghost_x, ghost_y = self.position
        player_x, player_y = player_position
        ghost_x += 1 if ghost_x < player_x else -1
        ghost_y += 1 if ghost_y < player_y else -1
        self.position = (ghost_x, ghost_y)
        return self.position

    def move_away_from(self, player_position):
        ghost_x, ghost_y = self.position
        player_x, player_y = player_position
        ghost_x -= 1 if ghost_x < player_x else 1
        ghost_y -= 1 if ghost_y < player_y else 1
        self.position = (ghost_x, ghost_y)
        return self.position
