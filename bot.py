#!/usr/bin/python
import sys
import time
import gtk
import pyautogui

def pixel_at(x, y):
    rw = gtk.gdk.get_default_root_window()
    pixbuf = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB, False, 8, 1, 1)
    pixbuf = pixbuf.get_from_drawable(rw, rw.get_colormap(), x, y, 0, 0, 1, 1)
    return tuple(pixbuf.pixel_array[0, 0])

def main():
    max_score = int(sys.argv[1])
    score = 0
    time.sleep(3)

    pyautogui.press(' ')

    time.sleep(2)

    while score < max_score:
        pixel_left = pixel_at(954, 567)
        pixel_right = pixel_at(1045, 567)
        if pixel_right[0] < pixel_left[0]:
            pyautogui.press('left', 2, interval=0.08)
        else:
            pyautogui.press('right', 2, interval=0.08)
	time.sleep(0.12)

        score += 2

if __name__ == "__main__":
    main()
