import MySQLdb


def connect_matches():
    db = MySQLdb.connect("localhost" , "root" , "cT$82!sE", "reaction_game_db")
    return db

def get_cursor():
    cursor = connect_ranked_match().cursor()
    return cursor

def insertRanked(name, avg, best):
    db = connect_matches()
    cursor = db.cursor()

    query = ("INSERT INTO ranked_matches (name, avg_time, best_time) VALUES ('%s', %f, %f);" % (name, avg, best))

    cursor.execute(query)
    db.commit()
    
    print("New entry added")
