'''Made by Joe Dunkin on 5/05/26 for no reason'''

import sqlite3

DB = "uhnime.db"

def print_all():
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    query = "SELECT * FROM Anime;"
    cursor.execute(query)
    answers = cursor.fetchall()
    print("Rank  Name                                                   Score   Genre  Episodes")
    for answer in answers:
        print(f"{answer[0]:<6}{answer[1]:<55}{answer[2]:<10}{answer[3]:<8}{answer[4]}")
    db.close

print_all()


