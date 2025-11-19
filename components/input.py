import sys

# ----- POSIX (Linux / macOS) -----
try:
    import termios, tty, select

    def getch_nonblock():
        dr, _, _ = select.select([sys.stdin], [], [], 0)
        if dr:
            fd = sys.stdin.fileno()
            old = termios.tcgetattr(fd)
            try:
                tty.setraw(fd)
                return sys.stdin.read(1)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old)
        return None  # no key pressed

# ----- Windows -----
except ImportError:
    import msvcrt

    def getch_nonblock():
        if msvcrt.kbhit():
            return msvcrt.getch().decode()
        return None
