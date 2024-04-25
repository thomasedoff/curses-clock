#!/usr/bin/env python3

import curses
from datetime import datetime
from zoneinfo import ZoneInfo
from chars import numbers, colon

def main(stdscr):
  timezone = ZoneInfo("Europe/Berlin")
  curses.curs_set(0)
  win_height, win_width = stdscr.getmaxyx()
  char_width = 9
  char_height = 7
  stdscr.timeout(1000)
  stdscr.resize(char_height,8*char_width)
  stdscr.mvwin((win_height//2)-(char_height//2),(win_width//2)-(8*char_width//2))

  windows = {}
  for i in range(1,9):
    windows[i] = stdscr.derwin(char_height,char_width,0,i*char_width-char_width)

  while True:
    current_time = datetime.now()
    formatted_time = current_time.strftime("%H:%M:%S")

    for i in range(1,9):
      if i in (3, 6):
        windows[i].addstr(0,0,colon)
      else:
        windows[i].addstr(0,0,numbers[int(formatted_time[i-1])])
      windows[i].refresh()

    try:
      key = stdscr.getkey()
      if key:
        break
    except curses.error:
      pass

if __name__ == "__main__":
  curses.wrapper(main)