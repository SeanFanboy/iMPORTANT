# insert cool docstring
# Imports
import sqlite3

# constants and variables
DATABASE = "task 7.db"

# functions
def print_all_aircraft():
    '''print all the aircraft nicely'''
    db= sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM Fighters;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all results
    print(f"Aircraft                      Speed  Max_G  Climb_Rate  Range  Payload")
    for result in results:
        print(f"{result[1]:<30}{result[2]:<8}{result[3]:<9}{result[4]:<9}{result[5]:<8}{result[6]:<6}")
    #finish loop
        db.close()



#main code
while True:
    user_input = input("\nWhat would you like do. \n1.Print all aircraft\n2.Exit \n")
    if user_input == '1':
        print_all_aircraft()
    elif user_input == '2':
        break
    else:
        print("That was not an option you FOOL\n")