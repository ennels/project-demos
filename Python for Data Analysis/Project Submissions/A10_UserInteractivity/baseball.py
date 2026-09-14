#!/usr/bin/env python3
# Elijah Walker - AICC 120 Assignment  - Mini Project C - Baseball Manager (Upgraded)

from pathlib import Path
import time
import os
from player import Player
from fileIO2 import read_csv, write_csv

path = Path("players.csv")
fieldnames_const = ['name', 'jersey', 'atbats', 'hits']
strikes = 0


def initialize_file():
    '''Initializes the CSV file.'''
    players = [
                Player('Billy Joe', 2, 18, 2),
                Player('Sammy Simms', 25, 10, 3),
                Player('Tim Thomas', 41, 16, 5),
                Player('Elijah Walker', 13, 400, 400)
            ]

    write_csv('players.csv', players, ['name', 'jersey', 'atbats', 'hits'])


def clear_terminal():
    '''Allows me to keep the terminal screen readable.'''
    if os.name == 'nt':
        _ = os.system('cls')  # For Windows

    else:
        _ = os.system('clear')  # For Linux/macOS


def handle_input(user_input):
    '''Handles user input commands.'''
    if user_input == 'q' or user_input == 'quit' or user_input == 'exit':
        quit()

    elif user_input == 'a' or user_input == 'add':
        add_player()

    elif user_input == 'd' or user_input == 'delete':
        delete_player()

    elif user_input == 'e' or user_input == 'edit':
        edit_player()

    else:
        print("\nInvalid command. Please try again.\n")
        time.sleep(3)
        constructive_feedback()


def add_player():
    '''Adds a new player to the CSV file.'''

    print("\nAdding a new player -\n")
    new_player = []

    try:
        new_player.append(str(input("\t\tName:\t\t").strip().title()))
        if new_player[0] in [item.name for item in read_csv(path)]:
            raise Exception("\nThere is already another player with that name!")

        new_player.append(int(input("\t\tJersey:\t\t").strip()))
        if new_player[1] in [item.jersey for item in read_csv(path)]:
            raise Exception("\nThere is already another player with that jersey!")

        new_player.append(int(input("\t\tAt Bats:\t").strip()))
        new_player.append(int(input("\t\tHits:\t\t").strip()))

        player_obj = Player(
            new_player[0],
            new_player[1],
            new_player[2],
            new_player[3]
        )

        players_list = read_csv(path)
        players_list.append(player_obj)
        write_csv(path, players_list, fieldnames_const)

    except ValueError:
        print("\nInvalid input type. Please try again.\n")
        time.sleep(3)
        constructive_feedback()
        return

    except Exception as e:
        print(e)
        time.sleep(3)
        constructive_feedback()
        return

    print("\nPlayer added successfully.\n")
    time.sleep(3)
    clear_terminal()


def delete_player():
    '''Deletes a player from the CSV file.'''
    try:
        delete_index = int(input("\nDelete player (index #): ").strip()) - 1
        players_list = read_csv(path)

        if delete_index < 0 or delete_index >= len(players_list):
            raise Exception("\nInvalid player reference. Please try again.\n")

        deleted_player = players_list.pop(delete_index)
        write_csv(path, players_list, fieldnames_const)
        print(f"\nPlayer '{deleted_player.name}' deleted successfully.\n")
        time.sleep(3)
        clear_terminal()

    except ValueError:
        print("\nInvalid input type. Please try again.\n")
        time.sleep(3)
        constructive_feedback()
        return

    except Exception as e:
        print(e)
        time.sleep(3)
        constructive_feedback()
        return


def edit_player():
    '''Edits a player's information in the CSV file.'''
    try:
        edit_index = int(input("\nEdit player (index #): ").strip()) - 1
        players_list = read_csv(path)

        if edit_index < 0 or edit_index >= len(players_list):
            raise Exception("\nInvalid player reference. Please try again.\n")

        players_edit = players_list[edit_index]
        print(f"\nEditing player '{players_edit.name}' -\n"
              "(Press Enter to skip fields)\n")

        response = input("\t\tName:\t\t").strip().title()
        if response != '':
            names_already = [p.name for p in players_list if p != players_edit]
            if response in names_already:
                raise Exception("\nThere is already another player with that name!")
            players_edit.name = response

        response = input("\t\tJersey:\t\t").strip()
        if response != '':
            new_jersey = int(response)
            jerseys_already = [p.jersey for p in players_list if p != players_edit]
            if new_jersey in jerseys_already:
                raise Exception("\nThere is already another player with that jersey!")
            players_edit.jersey = new_jersey

        response = input("\t\tAt Bats:\t").strip()
        if response != '':
            players_edit.atbats = int(response)

        response = input("\t\tHits:\t\t").strip()
        if response != '':
            players_edit.hits(int(response))

        write_csv(path, players_list, fieldnames_const)
        print("\nPlayer information updated successfully.\n")
        time.sleep(3)
        clear_terminal()

    except ValueError:
        print("\nInvalid input type. Please try again.\n")
        time.sleep(3)
        constructive_feedback()
        return

    except Exception as e:
        print(e)
        time.sleep(3)
        constructive_feedback()
        return


def display_stats():
    '''Reads player statistics from a CSV file and displays them.'''
    players = read_csv(path)
    print("\tJERSEY\tNAME\t\t\tAT-BATS\tHITS\tPCT\n")
    for player in players:
        player.display()


def constructive_feedback():
    '''Motivates the user to use their brain'''
    global strikes  # Found out how to use global variables online
    strikes += 1
    if strikes == 3:
        print("⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
              "⠇⡅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
              "⠧⡇⠀⠀⠒⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⡤⡆⠦⠆⢀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
              "⠧⣷⣆⠅⢦⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠈⠀⠀⠀⠀⠀⢤⣤⣆⢇⣶⣤⡤⡯⣦⣌⡡⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
              "⠷⣿⣷⣆⣐⡆⠀⠀⠀⠀⢀⠤⠊⠀⠀⢀⣠⣾⢯⣦⣴⣜⣺⣾⣿⣤⠟⠋⣷⢛⡣⠭⠢⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
              "⠯⣿⣷⢫⡯⠄⠀⠀⢀⠐⠁⠀⠀⠀⠠⣤⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣙⣷⡗⢤⡤⠀⠈⣰⠶⡤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
              "⣩⣿⡏⠉⠉⠀⢠⡔⠁⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠑⣏⠶⡉⠖⣡⠂⣈⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
              "⣮⣿⣧⣤⣤⠖⠁⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⢉⡻⣿⣿⣿⣿⣿⣿⣿⣿⠟⠓⠈⠅⠈⠀⠀⠘⢒⣽⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
              "⣿⡿⠛⠉⠀⠀⠀⣀⠔⢀⡴⣃⠀⠀⢀⠷⠲⡄⠸⠟⢋⣿⣿⣿⣿⣿⡇⠀⠀⠀⠐⠁⠀⠀⠂⠀⠀⠰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
              "⡆⣷⣆⡐⠶⠤⢤⣷⣀⣀⣩⢐⣟⣥⠜⣤⣀⣠⣤⠀⠈⠉⢀⣹⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
              "⢃⣿⣞⣫⡔⢆⡸⡿⣿⣿⣄⣰⣿⠁⢀⣛⠿⣻⣿⣿⣧⣬⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⢀\n"
              "⢼⣿⣟⢿⣧⣾⣵⣷⣿⣿⣟⡿⢿⣶⣞⣍⡴⢿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⣠⠈⠀⢀⣀⣼\n"
              "⠋⣿⣟⡛⢿⣿⣿⣿⣿⣿⣭⣿⣿⣿⣿⣯⣽⣿⣿⣿⣿⠟⠛⠿⢽⣿⣿⣆⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⣀⢀⡠⣤⣤⣰⣿⠟⠁⠀⠀⡼⢾⣿\n"
              "⣻⣿⣟⣇⠈⣉⣯⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠃⠀⠀⠀⠀⠀⠻⣿⣿⣿⣿⣴⣶⣤⣤⣤⣤⣴⣴⣴⣶⣦⣦⣤⣦⣀⣦⣤⣶⣿⣿⣿⣿⣿⣿⣿⠿⠁⠀⠀⡀⣤⣬⣾⣿\n"
              "⡝⣿⣿⣇⣤⣶⣿⣷⣾⣭⡿⠻⢿⣿⣿⣿⣿⠿⠃⠀⠀⠀⠀⡄⠀⠀⠀⢊⡻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠋⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⢿⠟⢉⠀⡀⢤⣴⣿⣿⣿⠿⠻\n"
              "⡁⣻⣿⣿⣿⣿⣷⣿⣿⣿⣿⠾⣿⡿⠞⠁⠀⠀⠀⠀⠀⠔⠫⡅⠀⠀⠀⠀⠁⣀⠀⠈⠻⣿⣿⣿⣿⣻⢟⣁⣄⡄⣀⠙⠻⣿⣿⡿⠿⠛⡋⠕⠂⢀⣀⣄⣓⣳⢿⠟⢛⣩⠴⠈⠀\n"
              "⠂⡁⠈⠛⠛⠛⠛⠋⠁⠀⠈⠈⡀⠀⠀⠀⠀⢀⠘⠀⠀⠀⠆⠀⡀⡢⣀⣆⠄⠈⠨⢦⡀⣈⠙⠛⠿⢿⣿⣿⣿⣿⣿⡿⡿⠿⠟⠆⠒⠁⠀⢶⣾⠿⠟⠛⢉⣀⣠⡶⠚⠁⠀⠀⣠\n"
              "⠀⡇⡄⣀⡀⠀⠀⠀⠀⠀⠀⠀⢬⠠⠀⡀⠀⠋⠁⠀⡀⠀⠀⡀⠆⢱⣿⣿⣧⣧⣄⠛⣿⣞⣵⣤⣷⣄⠀⠀⠀⠐⠀⠀⠀⠀⠀⠈⠉⠁⠁⠀⠠⢤⣶⣾⣿⡿⠋⢀⣀⣰⣶⣾⣿\n"
              "⡀⡆⠀⡉⡁⢿⣉⢀⠀⣰⣷⣿⣟⠠⡽⢂⡀⡄⠀⠰⣖⢱⢖⢂⡆⠈⣿⣿⣿⣿⣿⣶⣄⡙⠻⢿⣿⣿⣷⣦⣀⠀⠠⣤⣀⡀⢈⣓⣶⣶⣿⣿⣿⣿⣿⠟⠉⠀⠀⠀⣉⣭⣽⣿⣿\n"
              "⡇⣯⣿⣿⣿⣾⣿⣿⣿⠿⠟⡡⢞⣹⠾⢻⣚⣛⢺⠞⢋⣭⣾⣧⡃⢄⡈⢿⣿⣿⣿⣿⣿⣿⣯⣿⣮⣽⣿⣿⣿⣿⣷⣬⣽⣿⣿⣿⣽⡿⣿⡿⠟⠋⢀⣀⣐⣺⣿⣿⣟⣫⣭⣿⣿\n"
              "⢳⣿⣿⣿⣿⣿⣿⣿⣿⣤⣿⣿⣿⣿⣿⣦⠒⠉⢁⡀⠀⣙⣛⢿⣷⣶⣅⠀⠙⠻⣿⣿⣿⣿⣟⡚⠛⠻⠞⠿⠿⡿⡿⠯⠁⠟⣊⠾⠝⢋⣁⣀⣤⣤⣿⣿⣿⡿⠿⠿⠻⠛⠻⠻⠿\n"
              "⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣐⣾⡿⡟⢶⠾⢋⢹⠿⢿⣿⣿⣷⣦⡈⠙⠛⠿⠿⢿⣶⣶⣶⣶⣶⢶⠟⠚⠀⠁⠀⠀⠙⠛⠛⠛⠛⠛⠋⠉⠁⠀⠀⠀⠀⠀⢀⠀⠀\n\n")
        print(input("AVAST YE, MATEYS! THERE BE NO SAVVY MINDS IN THESE WATERS!\n"
                    "PRESS ENTER TO CONTINUE..."))
        strikes = 0
    clear_terminal()


def main():
    '''Main function.'''

    initialize_file()

    while True:
        clear_terminal()
        print("--------------------------------\n")
        print("Welcome to Baseball Manager!\n\n"
              "You are the manager of a baseball team, responsible for\n"
              "adding, deleting, and editing player information.\n\n"
              "Here is your current lineup:")
        print("\n--------------------------------\n")

        display_stats()
        print("\n--------------------------------")
        print("\nYou can modify the player list using the following commands:")

        print("\n--------------------------------\n")
        handle_input(input("\tAdd (A)\t\tAdd a player\n"
                           "\tDelete (D)\tDelete a player\n"
                           "\tEdit (E)\tEdit a player's info\n"
                           "\tQuit (Q)\tQuit program\n\n"
                           "--------------------------------\n"
                           "\nEnter a command: ").strip().lower())


if __name__ == "__main__":
    main()
