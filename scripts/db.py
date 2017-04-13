import MySQLdb


def connect_matches():
    db = MySQLdb.connect("localhost" , "root" , "cT$82!sE", "reaction_game_db")
    return db

def get_cursor():
    cursor = connect_ranked_match().cursor()
    return cursor

def insertUnranked(name, avg, best):

    db = connect_matches()
    cursor = db.cursor()
    
    
    r1 = "name"
    r2 = "avg_time"
    r3 = "best_time"
    
    query = ("INSERT INTO unranked_matches (name, avg_time, best_time) VALUES ('%s', %f, %f);" % (name, avg, best))


    cursor.execute(query)
    db.commit()
    
    print("Record added")


def insertRanked(name, avg, best):
    db = connect_matches()
    cursor = db.cursor()

    query = ("INSERT INTO ranked_matches (name, avg_time, best_time) VALUES ('%s', %f, %f);" % (name, avg, best))

    cursor.execute(query)
    db.commit()
    
    print("New entry added")
