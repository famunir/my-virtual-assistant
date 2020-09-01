import json
import sqlite3
import os

comments_file = "RC_2015-01"
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

def format_data(comment):
    comment = comment.replace("\n", " newlinechar ").replace("\r", " newlinechar ").replace('"',"'")
    return comment

def find_parent(pid):
    try:
        sql = "SELECT comment FROM parent_reply WHERE commet_id = '{}' LIMIT 1".format(pid)
        cursor.execute(sql)
        result = cursor.fetchone()
        if result != None:
            return result[0]
        else:
            return False
    except Exception as e:
        print ("find parent", e)
        return False


if __name__ == "__main__":
    create_table()


    # Cleaning the data
    row_counter = 0
    paired_counter = 0
    with open (os.path.join(path, comments_file), buffering = 1000) as comments:
        for row in comments:
            row_counter +=1
            comment = json.loads(row)
            parent_id = comment['parent_id']
            body = format_data(comment['body'])
            created_utc = comment['created_utc']
            score = comment['score']
            subreddit = comment['subreddit']
            parent_data = find_parent(parent_id)

            print (comment)
            break

        print(os.path.join(path,comments_file))