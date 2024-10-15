import curses

stdscr = curses.initscr()
curses.start_color()
curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
text = "This is a marquee text effect!"
for i in range(len(text)):
    stdscr.addstr(0, i, text[i], curses.color_pair(1))
    stdscr.refresh()
    stdscr.timeout(100)
    stdscr.getch()