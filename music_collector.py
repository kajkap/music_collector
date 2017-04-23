import csv
import os
import random
from datetime import datetime


def main():
    """Main function - Music Collector menu."""
    print("Welcome in the CoolMusic! Choose the action:")
    while True:
        print("""
         1) Add new album
         2) Find albums by artist
         3) Find albums by year
         4) Find musician by album
         5) Find albums by letter(s).
         6) Find albums by genre
         7) Calculate the age of all albums
         8) Choose random album by genre
         9) Show the amount of albums by artist
        10) Find the longest-time album
         0) Exit""")

        action = input()
        if action == "1":
            add_album()
        elif action == "2":
            find_by_artist()
        elif action == "3":
            find_by_year()
        elif action == "4":
            find_by_album()
        elif action == "5":
            find_by_letters()
        elif action == "6":
            find_by_genre()
        elif action == "7":
            albums_age()
        elif action == "8":
            random_by_genre()
        elif action == "9":
            how_many_albums()
        elif action == "10":
            longest_album()
        elif action == "0":
            quit()
        else:
            os.system('clear')
            print("Wrong command. Choose one number from the list.")


def music():
    """Read data from file and put them into music_list"""
    music_list = []
    with open("music.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if row and "|" in row[0]:  # ignore empty lines and wrong format strings
                new_row = row[0].split(" | ")
                music_list.append(((new_row[0], new_row[1]), (int(new_row[2]), new_row[3], new_row[4])))
        return music_list


def add_album():
    """Add new album to the file"""
    os.system('clear')
    print("Type the informations about new album.")
    while True:
        artist = input("name of artist: ")
        if len(artist) > 0:
            break
        else:
            print("You have to enter this information.")
    while True:
        album = input("name of album: ")
        if len(album) > 0:
            break
        else:
            print("You have to enter this information.")
    while True:
        year = input("year of release: ")
        if year.isdigit() and len(year) == 4:
            year = int(year)
            break
        else:
            print("Invalid input. Try again.")
    while True:
        genre = input("genre: ")
        if len(genre) > 0:
            break
        else:
            print("You have to enter this information.")
    while True:
        length = input("length(in format mm:ss): ")
        if len(length) >= 5:
            if length[:-3].isdigit() and length[-3] == ":" and length[-2:].isdigit():
                break
        else:
            print("Invalid input. Try again.")

    with open("music.csv", "a") as f:
        writer = csv.writer(f)
        writer.writerow(["%s | %s | %d | %s | %s" % (artist, album, year, genre, length)])
    print("\nPress enter to continue")
    input()
    os.system('clear')


def find_by_artist():
    """Search album by artist"""
    os.system('clear')
    music_list = music()
    name = input("Enter the name of the artist: ")
    occurrence = 0
    for item in music_list:
        if item[0][0].lower() == name.lower():
            print("%s: %s" % (item[0][0], item[0][1]))
            occurrence = 1
    if occurrence == 0:
        print("\nThere is no album of %s on this music list." % name)
    print("\nPress enter to continue")
    input()
    os.system('clear')


def find_by_year():
    """Search album by year"""
    os.system('clear')
    music_list = music()
    while True:
        year = input("Enter the year of the release of the album: ")
        if year.isdigit() and len(year) == 4:
            year = int(year)
            break
        else:
            print("Invalid input. Try again.")
    print("Albums from the year %d: " % year)
    occurrence = 0
    for item in music_list:
        if item[1][0] == year:
            print("%s - %s" % (item[0][0], item[0][1]))
            occurrence = 1
    if occurrence == 0:
        print("there is no album from this year on this music list.")
    print("\nPress enter to continue")
    input()
    os.system('clear')


def find_by_album():
    """Search musician by album"""
    os.system('clear')
    music_list = music()
    album = input("Enter the name of the album: ")
    occurrence = 0
    for item in music_list:
        if item[0][1].lower() == album.lower():
            print("%s: %s" % (item[0][0], item[0][1]))
            occurrence = 1
    if occurrence == 0:
        print("\nThere is no album '%s' on this music list." % album)
    print("\nPress enter to continue")
    input()
    os.system('clear')


def find_by_letters():
    """Search album by input letters"""
    os.system('clear')
    music_list = music()
    while True:
        letters = input("Write a part of the album's title: ")
        if len(letters) > 0 and letters != " ":
            break
        else:
            print("Invalid input. Try again.")
    occurrence = 0
    for item in music_list:
        if letters.lower() in item[0][1].lower():
            print("%s: %s" % (item[0][0], item[0][1]))
            occurrence = 1
    if occurrence == 0:
        print("There is no album with '%s' in the title." % letters)
    print("\nPress enter to continue")
    input()
    os.system('clear')


def find_by_genre():
    """Search albums by genre"""
    os.system('clear')
    music_list = music()
    genre = input("Enter the genre of the music: ")
    print("%s: " % genre)
    occurrence = 0
    for item in music_list:
        if item[1][1] == genre:
            print("%s - %s" % (item[0][0], item[0][1]))
            occurrence = 1
    if occurrence == 0:
        print("there is no album from this genre on this music list.")
    print("\nPress enter to continue")
    input()
    os.system('clear')


def albums_age():
    """Print the age of all albums"""
    os.system('clear')
    current_year = datetime.now().year
    music_list = music()
    print("The age of albums:")
    for item in music_list:
        album_age = current_year - item[1][0]
        print("%s: %s - %d years old" % (item[0][0], item[0][1], album_age))
    print("\nPress enter to continue")
    input()
    os.system('clear')


def random_by_genre():
    """Choose random album by genre"""
    os.system('clear')
    music_list = music()
    genre = input("Enter the genre of the music: ")
    print("%s album:" % genre)
    genre_list = []
    for item in music_list:
        if item[1][1].lower() == genre.lower():
            genre_list.append(item)
    if len(genre_list) > 0:
        album = random.choice(genre_list)
        print("%s - %s" % (album[0][0], album[0][1]))
    else:
        print("there is no %s album on this music list." % genre)
    print("\nPress enter to continue")
    input()
    os.system('clear')


def how_many_albums():
    """Print the amount of artist's albums"""
    os.system('clear')
    music_list = music()
    name = input("Enter the name of the artist: ")
    albums_amount = 0
    for item in music_list:
        if item[0][0].lower() == name.lower():
            albums_amount += 1
    if albums_amount == 1:
        print("%s: 1 album" % (item[0][0]))
    else:
        print("%s: %d albums" % (item[0][0], albums_amount))
    print("\nPress enter to continue")
    input()
    os.system('clear')


def longest_album():
    """Print the longest album"""
    os.system('clear')
    music_list = music()
    length_list = []
    for item in music_list:
        length_list.append(item[1][2])
    longest_index = length_list.index(max(length_list))
    print("The longest album: %s - %s %s" % (
        music_list[longest_index][0][0], music_list[longest_index][0][1], length_list[longest_index]))
    print("\nPress enter to continue")
    input()
    os.system('clear')


main()
