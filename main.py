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

def main():

    try:
        while True:
            ch = getch()
            if ch in ('q', '\x03'):
                break
            time.sleep(0.02)
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()
