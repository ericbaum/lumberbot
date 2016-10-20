#!/usr/bin/python
import sys
import time
import gtk
import pyautogui

def get_pixels():
    rw = gtk.gdk.get_default_root_window()
    pix1 = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB, False, 8, 1, 1)
    pix2 = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB, False, 8, 1, 1)
    pix1 = pix1.get_from_drawable(rw, rw.get_colormap(), 914, 670, 0, 0, 1, 1)
    pix2 = pix2.get_from_drawable(rw, rw.get_colormap(), 1005, 670, 0, 0, 1, 1)
    return pix1.pixel_array[0, 0][0], pix2.pixel_array[0, 0][0]

def main():
    max_score = int(sys.argv[1])
    score = 0
    time.sleep(3)

    pyautogui.press(' ')

    time.sleep(2)
    pyautogui.press('left', 2, 0.2)

    while score < max_score:
        pix1, pix2 = get_pixels()
	print str(pix1) + ' ' + str(pix2)
	if pix2 < pix1:
            pyautogui.press('left', 2, 0.06)
        elif pix2 > pix1:
            pyautogui.press('right', 2, 0.06)
	else:
            continue
	time.sleep(0.02)

        score += 2

if __name__ == "__main__":
    main()
