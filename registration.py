import random
import string
import hashlib
from colorama import Fore, Style, init
import time
import os
init()


def randuser():
    password = ""
    for _ in range(9):
        password += random.choice(string.ascii_letters)
    
    password2 = hashlib.sha256(password.encode()).hexdigest()
    with open("hashbase.txt", "a+") as file:
        file.seek(0)
        number = len(file.readlines()) + 1
        file.write(f"{password2} \n")

    return password, password2




start = input("Do you wish to Continue?: ")
if start.lower() in ["y",
                     "ye",
                     "yes"]:
    password, hashed = randuser()
    os.system("cls")
    print(f"Your generated password is:", Fore.GREEN + f"'{password}'" + Style.RESET_ALL)
    time.sleep(1)
    print(Fore.RED + "Please save it before continuing as you will not be able to recover!\n" + Style.RESET_ALL)
    time.sleep(3)