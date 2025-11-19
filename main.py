import sys, time

try:
    import termios, tty
    def getch():
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            return sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)
except ImportError:
    import msvcrt
    def getch():
        return msvcrt.getch().decode()

from components.player import PlayerCls
from components.world import WorldCls
from components.render import render, draw

def main():
    world = WorldCls(width=30, height=15)
    player = PlayerCls(world, x=15, y=7)

    try:
        while True:
            scene = render(world, player)
            draw(scene)
            ch = getch()
            if ch in ('q', '\x03'):
                break
            player.handle_input(ch)
            time.sleep(0.02)
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()
