'''Made by Joe Dunkin on 5/05/26 for no reason'''

import sqlite3

DB = "uhnime.db"

def print_all():
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    query = "SELECT * FROM Anime;"
    cursor.execute(query)
    answers = cursor.fetchall()
    for answer in answers:
        print(f"{answer[0]:<3}{answer[1]:<55}{answer[2]:<8}{answer[3]}")
    db.close

print_all()


