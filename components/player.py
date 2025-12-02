from components.world import WorldCls
from components.input import getch_nonblock, get_key

class PlayerCls:
    def __init__(self, world: WorldCls):
        self.world = world
        self.quit = False
        self.reset()

    def reset(self):
        self.x, self.y = self.world.width//2, self.world.height-2

    def handle_input(self, ch: str):
        # shooting
        if ch == b' ':
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

    def handle_key(self):
        ch = get_key()

        # quit
        if ch in (b'q', b'Q', b'\x03'):
            self.quit = True

        # reset
        if ch in (b'r', b'R'):
            self.reset()
            self.world.reset()

        # space
        elif ch == b' ':
            self.world.shoot_bullet(self.x, self.y)

        # WASD
        elif ch in (b'w', b'W'):
            if self.world.is_within(self.x, self.y - 1):
                self.y -= 1
        elif ch in (b's', b'S'):
            if self.world.is_within(self.x, self.y + 1):
                self.y += 1
        elif ch in (b'a', b'A'):
            if self.world.is_within(self.x - 1, self.y):
                self.x -= 1
        elif ch in (b'd', b'D'):
            if self.world.is_within(self.x + 1, self.y):
                self.x += 1

        # arrow keys (Linux + Windows)
        elif ch in (b'\x1b[A', b'\xe0H'):   # up
            if self.world.is_within(self.x, self.y - 1):
                self.y -= 1
        elif ch in (b'\x1b[B', b'\xe0P'):   # down
            if self.world.is_within(self.x, self.y + 1):
                self.y += 1
        elif ch in (b'\x1b[D', b'\xe0K'):   # left
            if self.world.is_within(self.x - 1, self.y):
                self.x -= 1
        elif ch in (b'\x1b[C', b'\xe0M'):   # right
            if self.world.is_within(self.x + 1, self.y):
                self.x += 1

        return ch
