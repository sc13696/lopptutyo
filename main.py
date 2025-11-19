import time

from components.input import getch
from components.player import PlayerCls
from components.world import WorldCls
from components.render import render, draw

def main():
    world = WorldCls(width=30, height=15)
    player = PlayerCls(world, x=15, y=15-2)

    try:
        while True:
            draw(render(world, player))
            time.sleep(0.05)
            ch = getch()
            if ch in ('q', '\x03'):
                break
            player.handle_input(ch)
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()
