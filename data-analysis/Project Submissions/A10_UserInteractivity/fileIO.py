import csv
from player import Player


def read_csv(file_path):    
    """Reads a CSV file and returns its content as a list of dictionaries.

    Args:
        file_path (str): The path to the CSV file.

    Returns:
        list: A list of dictionaries representing the rows in the CSV file.
    """
    with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        players = []
        for row in reader:
            player = Player(str(row['name']), int(row['jersey']), int(row['atbats']), int(row['hits']))
            # Had to edit this a bit so baseball.py picks up on incorrect data types during entries
            players.append(player)
        return players


def write_csv(file_path, players, fieldnames):    
    """Writes a list of dictionaries to a CSV file.

    Args:
        file_path (str): The path to the CSV file.
        data (list): A list of dictionaries representing the rows to be written.

    """
    with open(file_path, mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for player in players:
            writer.writerow({
                'name': player.name,
                'jersey': player.jersey,
                'atbats': player.atbats,
                'hits': player.hits
            })
