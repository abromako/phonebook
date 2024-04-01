import os
import sys


def add_new_user(name: str, phone: str, filename: str):
    """
    Dobavlenie novogo User
    """
    new_line = "\n" if read_all(filename) != "" else ""

    with open(filename, "a", encoding="utf-8") as file:
        file.write(f"{new_line} {name} - {phone}")


def read_all(filename: str) -> str:
    """
    Vozvrashaet vse soderzhimoe knigi
    """
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()


def search_user(filename: str, data: str) -> str:
    """
    Poisk zapisi po kriterijam data.
    """
    with open(filename, "r", encoding="utf-8") as file:
        list_1 = file.read().split("\n")
        res = list()

        res = [i for i in list_1 if data in i]

    if not res:
        return "No result"

    return "\n".join(res)


def transfer_record(source: str, destination: str, num_row: int):
    """
    Perenosit vibrannuju zapisj v drugoj fajl

    source str - imja ishodnogo fajla
    dest str - imja kuda perenosim
    num_row int - nomer perenosimoj stroki
    """
    new_line = "\n" if read_all(destination) != "" else ""

    with open(source, "r", encoding="utf-8") as file:
        lines = file.readlines()
        if num_row > len(lines):
            print("Nothing to move")
            return "pass"
        content = lines[num_row - 1]

    with open(destination, "a", encoding="utf-8") as file:
        file.write(f"{new_line} {content}")


INFO_STRING = """
Choose the option 
1 - Show all data 
2 - Add new user
3 - Search
4 - Move data
"""

kniga = "number.txt"
dest = "favourites.txt"

if kniga not in os.listdir():
    print("No such file or directory")
    sys.exit()


while True:
    mode = int(input(INFO_STRING))
    if mode == 1:
        print(read_all(kniga))
    elif mode == 2:
        name = str(input("Enter name:\n"))
        phone = str(input("Enter phone:\n"))
        add_new_user(name, phone, kniga)
    elif mode == 3:
        data = str(input("ener key:\n"))
        print(search_user(kniga, data))
    elif mode == 4:
        row = int(input("ener row to move:\n"))
        transfer_record(kniga, dest, row)






