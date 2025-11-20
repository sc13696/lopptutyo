
class WorldCls:
    def __init__(self, width: int = 20, height: int = 10):
        self.width, self.height = width, height
        self.aliens = [{"x": x, "y": y} for y in range(2,5) for x in range(5, width-5, 3)]
        self.bullets = []
        self.direction = 1  # move right

    def is_within(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height

    def update(self, ticks: int):
        # bullets move
        new_bullets = []
        for b in self.bullets:
            b["y"] -= 1
            if b["y"] >= 0:
                new_bullets.append(b)
        self.bullets = new_bullets

        # bullet–alien collisions
        survivors = []
        for al in self.aliens:
            hit = False
            for b in self.bullets:
                if b["x"] == al["x"] and b["y"] == al["y"]:
                    hit = True
                    b["y"] = -999
                    break
            if not hit:
                survivors.append(al)
        self.aliens = survivors

        # alien movement every few ticks
        if ticks % 15 == 0:
            for al in self.aliens:
                al["x"] += self.direction
            # bounce
            if any(a["x"] <= 1 or a["x"] >= self.width-2 for a in self.aliens):
                self.direction *= -1
                for a in self.aliens:
                    a["y"] += 1
