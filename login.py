import hashlib
from colorama import Fore, Style, init
import requests
import time
import os
init()

key = "sua chave aqui!"
loggedin = False
login = input("Password: ")
hashlogin = hashlib.sha256(login.encode()).hexdigest()

def Wgrab(city):
    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": "sua chave aqui!",
        "units": "metric"
    }

    response = requests.get(url, params=params)
    data = response.json()

    if response.status_code == 200:
        weather = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        print(f"\nWeather in {city}:")
        print(f"- Condition: {weather}")
        print(f"- Temperature: {temp}°C")
    else:
        print("Error:", data.get("message", "unknown error"))

with open("hashbase.txt", "r") as file:
    password = [line.strip() for line in file]

if hashlogin in password:
    print(Fore.GREEN + "Login accepted" + Style.RESET_ALL)
    loggedin = True
else:
    print(Fore.RED + "Incorrect Password " + Style.RESET_ALL)

if loggedin == True:
    os.system("cls")
    print(Fore.YELLOW + "Welcome to LockADashboard" + Style.RESET_ALL)
    time.sleep(1)
    try:
        while True:
            try:
                print(Fore.CYAN + "\n1 - Weather" + Style.RESET_ALL)
                print("\n2 - Quick commands")
                print(Fore.RED + "\n3 - Exit" + Style.RESET_ALL)
                opt = input(Fore.GREEN + "\nOption: " + Style.RESET_ALL)

                if opt == "1":
                    os.system("cls")
                    city = input("City: ")
                    Wgrab(city)

                elif opt == "2":
                    while True:
                        os.system("cls")
                        time.sleep(0.5)
                        print(Fore.LIGHTCYAN_EX + "\n1 - Ipconfig" + Style.RESET_ALL)
                        print(Fore.GREEN + "\n2 - windows version" + Style.RESET_ALL)
                        print(Fore.YELLOW + "\n3 - task managing" + Style.RESET_ALL)
                        print(Fore.BLUE + "\n4 - clear screen" + Style.RESET_ALL)
                        print(Fore.RED + "\n5 - Exit" + Style.RESET_ALL)
                        opt2 = input(Fore.GREEN + "\nOption: " + Style.RESET_ALL)

                        if opt2 == "1":
                            os.system("ipconfig")
                            time.sleep(2)
                            leave = input(Fore.BLUE + "\nContinue?: " + Style.RESET_ALL)
                            if leave.lower() in ["y",
                                                 "ye",
                                                 "yes"]:
                                os.system("cls")
                                pass

                            else:
                                os.system("cls")
                                break
                        
                        elif opt2 == "2":
                            os.system("ver")
                            time.sleep(1)
                            leave = input(Fore.BLUE + "\nContinue?: " + Style.RESET_ALL)
                            if leave.lower() in ["y",
                                                 "ye",
                                                 "yes"]:
                                os.system("cls")
                                pass

                            else:
                                os.system("cls")
                                break

                        elif opt2 == "3":
                            os.system("tasklist")
                            time.sleep(3)
                            leave = input(Fore.BLUE + "\nContinue?: " + Style.RESET_ALL)
                            if leave.lower() in ["y",
                                                 "ye",
                                                 "yes"]:
                                os.system("cls")
                                pass

                            else:
                                os.system("cls")
                                break
                        
                        elif opt2 == "4":
                            os.system("cls")
                            time.sleep(0.3)
                            leave = input(Fore.BLUE + "\nContinue?: " + Style.RESET_ALL)
                            if leave.lower() in ["y",
                                                 "ye",
                                                 "yes"]:
                                os.system("cls")
                                pass

                            else:
                                os.system("cls")
                                break
                                
                        
                        elif opt2 == "5":
                            os.system("cls")
                            time.sleep(0.5)
                            break


                elif opt == "3":
                    os.system("cls")
                    exit()

                else:
                    os.system("cls")
                    print(Fore.RED + "Error" + Style.RESET_ALL)
                    time.sleep(2)
                    os.system("cls")

            except ValueError:
                print("ERROR")
            



    except ValueError:
        print("ERROR")
    