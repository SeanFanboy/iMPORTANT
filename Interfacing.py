'''Made by Joe Dunkin on 5/05/26 for no reason'''

import sqlite3

DB = "uhnime.db"

def print_all():
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    query = "SELECT Anime.Ranking, Anime.Name, Anime.Score, Genres.Genre_name, Anime.Episodes FROM Anime  JOIN Genres ON Anime.Genre_ID = Genres.ID;"  
    cursor.execute(query)
    answers = cursor.fetchall()
    print("Rank  Name                                                   Score     Genre        Episodes")
    for answer in answers:
        print(f"{answer[0]:<6}{answer[1]:<55}{answer[2]:<10}{answer[3]:<15}{answer[4]}")
    db.close

def print_all_seinen():
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    query = "SELECT Anime.Ranking, Anime.Name, Anime.Score, Genres.Genre_name, Anime.Episodes FROM Anime  JOIN Genres ON Anime.Genre_ID = Genres.ID WHEN Genre_ID = 1;"  
    cursor.execute(query)
    answers = cursor.fetchall()
    print("Rank  Name                                                   Score     Genre        Episodes")
    for answer in answers:
        print(f"{answer[0]:<6}{answer[1]:<55}{answer[2]:<10}{answer[3]:<15}{answer[4]}")
    db.close

def print_all_romance():
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    query = "SELECT Anime.Ranking, Anime.Name, Anime.Score, Genres.Genre_name, Anime.Episodes FROM Anime  JOIN Genres ON Anime.Genre_ID = Genres.ID;"  
    cursor.execute(query)
    answers = cursor.fetchall()
    print("Rank  Name                                                   Score     Genre        Episodes")
    for answer in answers:
        print(f"{answer[0]:<6}{answer[1]:<55}{answer[2]:<10}{answer[3]:<15}{answer[4]}")
    db.close

def print_all_shonen():
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    query = "SELECT Anime.Ranking, Anime.Name, Anime.Score, Genres.Genre_name, Anime.Episodes FROM Anime  JOIN Genres ON Anime.Genre_ID = Genres.ID;"  
    cursor.execute(query)
    answers = cursor.fetchall()
    print("Rank  Name                                                   Score     Genre        Episodes")
    for answer in answers:
        print(f"{answer[0]:<6}{answer[1]:<55}{answer[2]:<10}{answer[3]:<15}{answer[4]}")
    db.close

def print_all_fantasy():
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    query = "SELECT Anime.Ranking, Anime.Name, Anime.Score, Genres.Genre_name, Anime.Episodes FROM Anime  JOIN Genres ON Anime.Genre_ID = Genres.ID;"  
    cursor.execute(query)
    answers = cursor.fetchall()
    print("Rank  Name                                                   Score     Genre        Episodes")
    for answer in answers:
        print(f"{answer[0]:<6}{answer[1]:<55}{answer[2]:<10}{answer[3]:<15}{answer[4]}")
    db.close

def print_all_comedy():
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    query = "SELECT Anime.Ranking, Anime.Name, Anime.Score, Genres.Genre_name, Anime.Episodes FROM Anime  JOIN Genres ON Anime.Genre_ID = Genres.ID;"  
    cursor.execute(query)
    answers = cursor.fetchall()
    print("Rank  Name                                                   Score     Genre        Episodes")
    for answer in answers:
        print(f"{answer[0]:<6}{answer[1]:<55}{answer[2]:<10}{answer[3]:<15}{answer[4]}")
    db.close

def print_all_slice_of_life():
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    query = "SELECT Anime.Ranking, Anime.Name, Anime.Score, Genres.Genre_name, Anime.Episodes FROM Anime  JOIN Genres ON Anime.Genre_ID = Genres.ID;"  
    cursor.execute(query)
    answers = cursor.fetchall()
    print("Rank  Name                                                   Score     Genre        Episodes")
    for answer in answers:
        print(f"{answer[0]:<6}{answer[1]:<55}{answer[2]:<10}{answer[3]:<15}{answer[4]}")
    db.close



while True:
    user_input = input("What genre would you like to explore?\n1. Seinen\n2. Romance\n3. Shonen\n4. Fantasy\n5. Comedy\n6. Slice Of Life\n7. Print all\n8. Close the database\n")

    if user_input == '1':
        print_all_seinen  
    elif user_input == '2':
        print('placeholder')
    elif user_input == '3':
        print('placeholder')
    elif user_input == '4':
        print('placeholder')
    elif user_input == '5':
        print('placeholder')
    elif user_input == '6':
        print('placeholder')
    elif user_input == '7':
        print_all()
    elif user_input =='8':
        break
    else:
        print("That wasn't an option!")

