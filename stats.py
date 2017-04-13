import db
###########################################################
## print stats ############################################
## such as number of unranked/ranked matches ##############
## ranking table(sortable by best_time and average_time) ##
###########################################################
def print_stats():
      ranked_matches = 0
      unranked_matches =0
      ##
      dbase = db.connect_matches()
      dcursor = dbase.cursor()

      query = "SELECT COUNT(ID) FROM ranked_matches"

      dcursor.execute(query)

      ranked_matches = dcursor.fetchall()

      ##
      print "Total ranked matches played : %d" %  ranked_matches[0]

