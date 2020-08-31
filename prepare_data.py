import json
import sqlite3
import os


comments_time = "2015-01"
sql_bulk = []
conn = None
db_name = '{}.db'.format(comments_time)
path = os.getcwd()
db_path = os.path.join(path, db_name)

#print(db_path)

conn = sqlite3.connect('{}.db'.format(comments_time))
cursor = conn.cursor()

def create_table():
    cursor.execute("""CREATE TABLE IF NOT EXISTS parent_reply
                    (parent_id TEXT PRIMARY KEY, comment_id TEXT UNIQUE, parent TEXT,
                    comment TEXT, subreddit TEXT, unix INT, score INT) """)


if __name__ == "__main__":
    create_table()


    # Cleaning the data