'''Made by Joe Dunkin on 5/05/26 to display animes I have watched based on genre'''
#importing required stuff
import sqlite3
#Defining important variables
DB = "uhnime.db"
#starting to define all the functions needed

#Defining a function that grabs all the information from the database
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

#defining a function that grabs all animes that fit in the seinen genre
def print_all_seinen():
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    query = "SELECT Anime.Ranking, Anime.Name, Anime.Score, Genres.Genre_name, Anime.Episodes FROM Anime  JOIN Genres ON Anime.Genre_ID = Genres.ID WHERE Genre_ID = 1;"  
    cursor.execute(query)
    answers = cursor.fetchall()
    print("Rank  Name                                                   Score     Genre        Episodes")
    for answer in answers:
        print(f"{answer[0]:<6}{answer[1]:<55}{answer[2]:<10}{answer[3]:<15}{answer[4]}")
    db.close

#defining a function that grabs all animes that fit in the romance genre
def print_all_romance():
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    query = "SELECT Anime.Ranking, Anime.Name, Anime.Score, Genres.Genre_name, Anime.Episodes FROM Anime  JOIN Genres ON Anime.Genre_ID = Genres.ID WHERE Genre_ID = 2;"  
    cursor.execute(query)
    answers = cursor.fetchall()
    print("Rank  Name                                                   Score     Genre        Episodes")
    for answer in answers:
        print(f"{answer[0]:<6}{answer[1]:<55}{answer[2]:<10}{answer[3]:<15}{answer[4]}")
    db.close

#defining a function that grabs all animes that fit in the shonen genre
def print_all_shonen():
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    query = "SELECT Anime.Ranking, Anime.Name, Anime.Score, Genres.Genre_name, Anime.Episodes FROM Anime  JOIN Genres ON Anime.Genre_ID = Genres.ID WHERE Genre_ID = 3;"  
    cursor.execute(query)
    answers = cursor.fetchall()
    print("Rank  Name                                                   Score     Genre        Episodes")
    for answer in answers:
        print(f"{answer[0]:<6}{answer[1]:<55}{answer[2]:<10}{answer[3]:<15}{answer[4]}")
    db.close

#defining a function that grabs all animes that fit in the fantasy genre
def print_all_fantasy():
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    query = "SELECT Anime.Ranking, Anime.Name, Anime.Score, Genres.Genre_name, Anime.Episodes FROM Anime  JOIN Genres ON Anime.Genre_ID = Genres.ID WHERE Genre_ID = 4;"  
    cursor.execute(query)
    answers = cursor.fetchall()
    print("Rank  Name                                                   Score     Genre        Episodes")
    for answer in answers:
        print(f"{answer[0]:<6}{answer[1]:<55}{answer[2]:<10}{answer[3]:<15}{answer[4]}")
    db.close

#defining a function that grabs all animes that fit in the comedy genre
def print_all_comedy():
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    query = "SELECT Anime.Ranking, Anime.Name, Anime.Score, Genres.Genre_name, Anime.Episodes FROM Anime  JOIN Genres ON Anime.Genre_ID = Genres.ID WHERE Genre_ID = 5;"  
    cursor.execute(query)
    answers = cursor.fetchall()
    print("Rank  Name                                                   Score     Genre        Episodes")
    for answer in answers:
        print(f"{answer[0]:<6}{answer[1]:<55}{answer[2]:<10}{answer[3]:<15}{answer[4]}")
    db.close

#defining a function that grabs all animes that fit in the slice of life genre
def print_all_slice_of_life():
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    query = "SELECT Anime.Ranking, Anime.Name, Anime.Score, Genres.Genre_name, Anime.Episodes FROM Anime  JOIN Genres ON Anime.Genre_ID = Genres.ID WHERE Genre_ID = 6;"  
    cursor.execute(query)
    answers = cursor.fetchall()
    print("Rank  Name                                                   Score     Genre        Episodes")
    for answer in answers:
        print(f"{answer[0]:<6}{answer[1]:<55}{answer[2]:<10}{answer[3]:<15}{answer[4]}")
    db.close


#While loop to make using the good easier for the user
while True:
    #Storing what they want to do via a variable
    user_input = input("What genre would you like to explore?\n1. Seinen\n2. Romance\n3. Shonen\n4. Fantasy\n5. Comedy\n6. Slice Of Life\n7. Print all\n8. Close the database\n")

    #If and elif stack to determine what to do with the user input
    if user_input == '1':
        print_all_seinen()  
    elif user_input == '2':
        print_all_romance()
    elif user_input == '3':
        print_all_shonen()
    elif user_input == '4':
        print_all_fantasy()
    elif user_input == '5':
        print_all_comedy()
    elif user_input == '6':
        print_all_slice_of_life()
    elif user_input == '7':
        print_all()
    #break condition
    elif user_input =='8':
        print("Database Closed")
        break
    #catchall in case silly humans try to break my code
    else:
        print("That wasn't an option!")