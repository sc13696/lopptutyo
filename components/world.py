
class WorldCls:
    def __init__(self, width: int = 20, height: int = 10):
        self.width, self.height = width, height

    def is_within(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height
