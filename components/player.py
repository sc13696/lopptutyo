from collections import defaultdict
from components.world import WorldCls

class PlayerCls:
    def __init__(self, world: WorldCls, x: int = 0, y: int = 0):
        self.world = world
        self.x, self.y = x, y
        self.keys = defaultdict(
            lambda: (0, 0),
            {
                'w': (0, -1),
                's': (0, 1),
                'a': (-1, 0),
                'd': (1, 0),
            }
        )

    def handle_input(self, ch: str):
        # shooting
        if ch == ' ':
            self.world.bullets.append({"x": self.x, "y": self.y - 1})
            return True
        # movement
        dx, dy = self.keys[ch]
        if dx == 0 and dy == 0:
            return False
        nx, ny = self.x + dx, self.y + dy
        if self.world.is_within(nx, ny):
            self.x, self.y = nx, ny
        return True
