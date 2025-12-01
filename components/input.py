import sys, os

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
                return os.read(fd, 1)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old)
        return None  # no key pressed

# ----- Windows -----
except ImportError:
    import msvcrt

    def getch_nonblock():
        if msvcrt.kbhit():
            return msvcrt.getch()
        return None






import sys, os

# ---------- Windows ----------
try:
    import msvcrt

    def get_key():
        if not msvcrt.kbhit():
            return None

        c = msvcrt.getch()

        if c in (b'\x00', b'\xe0'):
            return c + msvcrt.getch()     # arrow, f-keys

        return c                          # normal byte

# ---------- Linux / POSIX ----------
except ImportError:
    import termios, tty, select

    def get_key():
        dr,_,_ = select.select([sys.stdin], [], [], 0)
        if not dr:
            return None

        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            c = os.read(fd, 1)

            if c == b'\x1b':              # possible arrow sequence
                seq = c
                while True:
                    r,_,_ = select.select([sys.stdin], [], [], 0)
                    if not r:
                        break
                    seq += os.read(fd, 1)
                return seq                # e.g. b'\x1b[A'
            return c

        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)
