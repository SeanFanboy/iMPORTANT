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

print_all()


