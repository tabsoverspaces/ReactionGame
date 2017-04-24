import mysql.connector
import os

def connect_matches():
    db = mysql.connector.connect(user='root', password='cT$82!sE',host='localhost',database='reaction_game')
    
    return db

def get_cursor():
    cursor = connect_ranked_match().cursor()
    return cursor

def update_unranked_matches():
    
    fileDir = os.path.dirname(os.path.realpath('__file__'))
    filename = os.path.join(fileDir, '../data/unranked_matches_played.txt')

    file = open(filename, 'a+')
    file.seek(0)
    
    line = file.readline()
    number = int(line)
    
    number += 1

    file.truncate(0)

    file.write(str(number))

    file.close()

def insert_time(name, avg, best):
    db = connect_matches()
    cursor = db.cursor()

    query = ("INSERT INTO ranking (name, avg_time, best_time) VALUES ('%s', %f, %f);" % (name, avg, best))

    cursor.execute(query)
    db.commit()
    
    print("New entry added")

def insert_match(winner, p1, p2, p1score, p2score):
    db = connect_matches()
    cursor = db.cursor()

    query = ("INSERT INTO ranked_matches(player1, player2, player1score,player2score,winner,date) \
VALUES('%s','%s', %d, %d,'%s', CURDATE())" % (str(p1.name), str(p2.name), p1score,p2score, str(winner.name)))

    cursor.execute(query)
    db.commit()
    
