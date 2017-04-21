#! /usr/bin/python3.4

import pymysql
import random

#cursor = conn.cursor()

#cursor.execute("SELECT * FROM ranking")
#data = cursor.fetchall()


def load_names():
    
    name_list = list()

    for line in names:
        name_list.append(line)

    return name_list

def get_random_best():
    best_time = random.uniform(0.2 , 0.4)
    return best_time

def get_random_avg():
    avg_time = random.uniform(0.25,0.5)
    return avg_time
    

def fill_table():
    conn = pymysql.connect(user='root', password='',
                               host='localhost', database='reaction_game')

    names = open('names.txt', 'r')

    for line in names:
        name = line
        best = get_random_best()
        avg = get_random_avg()

        query = "INSERT INTO ranking(name, best_time, avg_time) VALUES('{0}','{1}','{2}')".format(name,best , avg)

        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()

        
fill_table()
