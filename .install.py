# Tool Name: Tool-X
# Author: Netzeros
# Date: 1/11/2017
# Powered By: Aex Software's

import os
import sys
from time import sleep

if os.path.exists("/usr/bin/yum"):
    if os.path.exists("/usr/lib/sudo"):
        system = "fedora"
        home_path = os.getenv("HOME") + "/"
        bin_path = "/usr/bin/"
        package_manager = "sudo yum"
    else:
        system = "fedora"
        home_path = os.getenv("HOME") + "/"
        bin_path = "/usr/bin/"
        package_manager = "yum"

elif os.path.exists("/usr/bin/apt"):
    if os.path.exists("/usr/lib/sudo"):
        system = "ubuntu"
        home_path = os.getenv("HOME") + "/"
        bin_path = "/usr/bin/"
        package_manager = "sudo apt-get"
    else:
        system = "debian"
        home_path = os.getenv("HOME") + "/"
        bin_path = "/usr/bin/"
        package_manager = "apt-get"

elif os.path.exists("/data/data/com.termux/files/usr/bin/pkg"):
    system = "termux"
    home_path = os.getenv("HOME") + "/"
    bin_path = "/data/data/com.termux/files/usr/bin/"
    package_manager = "pkg"

elif os.path.exists("/usr/bin/brew"):
    system = "mac"
    home_path = os.getenv("HOME") + "/"
    bin_path = "/usr/bin/"
    package_manager = "brew"

elif os.path.exists("/bin/brew"):
    system = "mac"
    home_path = os.getenv("HOME") + "/"
    bin_path = "/bin/"
    package_manager = "brew"

def exit_tool():
    sys.exit()

def clear_screen():
    os.system("clear")

def install_tool():
    if system == "termux":
        print("""\033[01;33m ===============================================
\033[01;32m|_________________ Installing __________________|
\033[01;33m ===============================================\033[00m""")
    else:
        print("""\033[01;33m =========================================================
\033[01;32m|_______________________ Installing ______________________|
\033[01;33m==========================================================\033[00m""")

def error_message():
    if system == "termux":
        clear_screen()
        print('''
\033[1;33m
          _____           _    __  __
         |_   _|__   ___ | |   \ \/ /
           | |/ _ \ / _ \| |____\  /
           | | (_) | (_) | |____/  \     
           |_|\___/ \___/|_|   /_/\_\ \033[1;m\033[1;91mv2.0\033[1;m


\033[1;36m ===============================================
\033[1;33m|           Install Best Hacking Tool           |
\033[1;36m ===============================================\033[1;m

\033[1;31m  [ + ]  \033[1;31mWe can't install Tool-X.\033[1;m
\033[1;31m  [ + ]  \033[1;31mThere are some errors.\033[1;m
\033[1;31m  [ + ]  \033[1;31mPlease try again later.\033[1;m
\033[1;36m_________________________________________________
=================================================\033[1;m
''')
    else:
        clear_screen()
        print('''
\033[1;33m
               _____           _    __  __
              |_   _|__   ___ | |   \ \/ /
                | |/ _ \ / _ \| |____\  /
                | | (_) | (_) | |____/  \     
                |_|\___/ \___/|_|   /_/\_\ \033[1;31mv2.0
\033[1;m

\033[1;36m ==========================================================
\033[1;33m|               \033[1;32m Install Best Hacking Tool.\033[1;33m               \033[1;33m|
\033[1;36m ==========================================================\033[1;m

\033[1;31m  [ + ]  \033[1;31mWe can't install Tool-X.\033[1;m
\033[1;31m  [ + ]  \033[1;31mThere are some errors.\033[1;m
\033[1;31m  [ + ]  \033[1;31mPlease try again later.\033[1;m
\033[1;36m___________________________________________________________
===========================================================\033[1;m
''')

def logo():
    if system == "termux":
        print('''
\007\033[1;33m
          _____           _    __  __
         |_   _|__   ___ | |   \ \/ /
           | |/ _ \ / _ \| |____\  /
           | | (_) | (_) | |____/  \     
           |_|\___/ \___/|_|   /_/\_\ \033[1;m\033[1;91mv2.0


\033[1;36m ===============================================
\033[1;33m|           \033[1;31m Notice for You from Tool-X.         \033[1;33m|
\033[1;36m ===============================================

\033[1;33m  [ + ] \033[1;32mUse it at your own risk.
\033[1;33m  [ + ] \033[1;32mNo warranty.
\033[1;33m  [ + ] \033[1;32mUse it for legal purposes only.
\033[1;33m  [ + ]
