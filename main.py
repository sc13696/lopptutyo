import time

from components.player import PlayerCls
from components.world import WorldCls
from components.render import render, draw

def main():
    world = WorldCls(width=30, height=10)
    player = PlayerCls(world)
    ticks = 0

    try:
        while not player.quit:
            draw(render(world, player))
            '''
            ch = getch_nonblock()
            if ch:
                if ch in (b'q', b'\x03'):
                    break
                player.handle_input(ch)
            '''
            world.update(ticks)
            ticks += 1
            player.handle_key()
            time.sleep(1/25)
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()
