#!/usr/bin/env python

#from os import system
import curses

import traceback

class App:

    def __init__(self):
        self.x = ord('m')
        self.param = -1
        self.screen = curses.initscr()
        self.__init_colors()

        
    def run(self):
        """
        Main method
        """
        try:
             # break out of loop if "q" key is pressed
            while self.x != ord('q'):
                curses.noecho()
                curses.cbreak()
                self.screen.clear()
                self.screen.border(0)

                self.screen.addstr(2, 2,
                                       "Press (0) Apache (1) Mysql (2) Samba (Q). To quit ",
                                       curses.A_STANDOUT)
                try:
                    curses.echo()
                    self.param = int(self.screen.getstr(5, 2, 60))
                except ValueError:
                     #self.x = self.screen.getch()
                     self.screen.addstr(4, 2, "Invalid value! (Press Enter)", curses.color_pair(3))
                     #self.screen.clear()
                     continue

                curses.noecho()

                #if parameter value received from the input
                if self.param > -1:
                    cmdRunner = CommandRunner(self.param)
                    cmdRunner.displayOptions(self.screen)

                self.screen.refresh()
                self.x = self.screen.getch()
        finally:
            self.screen.keypad(0)
            curses.echo()
            curses.nocbreak()
            curses.endwin()
            traceback.print_exc()           # Print the exception


    def __init_colors(self):
        """
        Initializes colors for text
        """
        curses.start_color()
        curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLUE)
        curses.init_pair(3, curses.COLOR_RED, curses.COLOR_WHITE)

class CommandRunner:

    options = [
        ("apache", ("start", "stop", "restart", "reload")),
        ("mysql", ("start", "stop", "restart", "reload")),
        ("samba", ("start", "stop", "restart", "reload"))
    ]

    def __init__(self, command_idx):
        if command_idx > len(CommandRunner.options)-1:
            raise IndexError("Index out of range of options array! " + str(command_idx))

        self.command_idx = command_idx

    # displays a list of options available for a given Unix command
    # list of options is set manually by the user of the program
    def displayOptions(self, _screen):
        optionName = CommandRunner.options[self.command_idx][0]
        _screen.addstr(5, 5, "***  %s chosen ***" % optionName, curses.A_BLINK)
        _screen.border(10)

        tplOptions = CommandRunner.options[self.command_idx][1]
        i = 10
        j = 0
        for strOpt in tplOptions:
            _screen.addstr(i, 30, "%d) %s " % (j, strOpt), curses.color_pair(2))
            i += 1
            j += 1

        optionNum = -1
        _screen.addstr(i - len(tplOptions) - 2, 30, "Select option number:", curses.color_pair(1))

        curses.echo()

        try:
            optionNum = int(_screen.getstr(i - len(tplOptions) - 2, 55, 60))
        except ValueError:
            _screen.addstr(4, 2, "Invalid value! (Press Enter)", curses.color_pair(3))
        _screen.clear()
        _screen.addstr(5, 5, "***  %s %s chosen ***" % (optionName, tplOptions[optionNum]), curses.A_BLINK)
        curses.noecho()



if __name__ == "__main__":
    app = App()
    app.run()
