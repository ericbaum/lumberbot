#!/usr/bin/python3
import sys
import time
import pyautogui
import gi
gi.require_version('Gdk', '3.0')
from gi.repository import Gdk

w = Gdk.get_default_root_window()


def pixel_at(x, y):
    pb = Gdk.pixbuf_get_from_window(w, x, y, 1, 1)
    return pb.get_pixels()


def main():
    max_score = int(sys.argv[1])
    score = 0
    time.sleep(3)

    pyautogui.press(' ')

    time.sleep(2)

    while score < max_score:
        pixel_left = pixel_at(916, 618)
        pixel_right = pixel_at(1016, 618)

        if pixel_right[0] < pixel_left[0]:
            pyautogui.press('left', 2, interval=0.09)
        else:
            pyautogui.press('right', 2, interval=0.09)

        score += 2

if __name__ == "__main__":
    main()
