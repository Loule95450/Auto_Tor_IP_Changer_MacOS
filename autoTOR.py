import time
import os
import subprocess
import argparse


def install_package(package_name, install_command):
    try:
        subprocess.check_output(f"which {package_name}", shell=True)
    except subprocess.CalledProcessError:
        print(f"[+] {package_name} is not installed !")
        subprocess.check_output(install_command, shell=True)
        print(f"[!] {package_name} is installed succesfully ")


def install_python_module(module_name):
    try:
        __import__(module_name)
    except ImportError:
        print(f"[+] python3 {module_name} is not installed")
        os.system(f"pip3 install {module_name}")


def change_ip():
    os.system("brew services restart tor")
    print("[+] Your IP has been Changed")


install_package("tor", "brew install tor")
install_python_module("requests")

os.system("brew services start tor")
time.sleep(3)

parser = argparse.ArgumentParser(description="Auto Tor IP Changer")
parser.add_argument(
    "-d", "--delay", type=int, default=60, help="Time to change IP in seconds"
)
parser.add_argument(
    "-l",
    "--loop",
    type=int,
    default=0,
    help="How many time do you want to change your IP",
)
args = parser.parse_args()
x, lin = args.delay, args.loop

print(
    """\033[1;32m \n
                _          _______
     /\        | |        |__   __|
    /  \  _   _| |_ ___      | | ___  _ __
   / /\ \| | | | __/ _ \     | |/ _ \| '__|
  / ____ \ |_| | || (_) |    | | (_) | |
 /_/    \_\__,_|\__\___/     |_|\___/|_|
                V 3.1
from mrFD & Loule for MacOS Compatability
Check in https://check.torproject.org/ if you are using Tor IP
"""
)
print("\033[1;31m https://loule.me/\n")
print(
    "\033[1;31m [+] You change your IP every "
    + str(x)
    + " seconds during "
    + str(lin)
    + " times\n"
)

if int(lin) == 0:
    while True:
        try:
            change_ip()
            time.sleep(int(x))
        except KeyboardInterrupt:
            print("\n[!] Exiting...")
            quit()
else:
    for i in range(int(lin)):
        time.sleep(int(x))
        change_ip()
