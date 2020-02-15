from util import tap_screen
import time


def tap_sleep(x,y):
    tap_screen(x,y)

    time.sleep(0.1)


if __name__ == '__main__':
    while True:
        tap_sleep(1700, 880)
        tap_sleep(2080, 980)
