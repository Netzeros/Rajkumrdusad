# Tool Name: Tool Kit
# Author: Netzeros
# Date: 28/4/2018
# Powered By: Aex Software's

import sys
from modules.logo import exit
from modules.menu import ToolX

class CheckOS(object):
    def check(self):
        if "linux" in sys.platform:
            # Running Tool Kit on Linux ...
            pass
        elif "darwin" in sys.platform:
            # Running Tool Kit on macOS ...
            pass
            # print("Sorry, it's not available for macOS right now...")
            exit()
        elif "win" in sys.platform:
            print("Sorry, it's not available for Windows right now...")
            exit()
        else:
            print("Tool Kit does not support '%s' right now!!!" % sys.platform)

def main():
    try:
        CheckOS().check()
        ToolX()
    except KeyboardInterrupt:
        exit()

if __name__ == "__main__":
    main()
