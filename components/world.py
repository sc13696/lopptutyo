
class WorldCls:
    def __init__(self, width: int = 20, height: int = 10):
        self.width = width
        self.height = height
        self.walls = set()
        for x in range(width):
            self.walls.add((x, 0))
            self.walls.add((x, height-1))
        for y in range(height):
            self.walls.add((0, y))
            self.walls.add((width-1, y))

    def is_blocked(self, x: int, y: int):
        return (x, y) in self.walls
    
    def can_move(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height
