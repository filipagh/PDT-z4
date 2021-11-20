# func to exec basic select
import psycopg2
from psycopg2.extras import RealDictCursor

""" Connect to the PostgreSQL database server """
conn = None


def get_hastags_for_tweet(tweet_id):
    sql_hastag = f'select distinct value from hashtags ' \
                 f'join tweet_hashtags th on hashtags.id = th.hashtag_id where th.tweet_id = \'{tweet_id}\''
    return exec_sql(sql_hastag)

def get_retweets_for_tweet(tweet_id):
    sql_hastag = f'select id from tweets where parent_id = \'{tweet_id}\''
    return exec_sql(sql_hastag)

def exec_sql(sql: str):
    try:
        conn = psycopg2.connect("dbname=tweets_db user=postgres password=root host=172.26.0.3")
        cur = conn.cursor(cursor_factory=RealDictCursor)

        cur.execute(sql)
        result = cur.fetchall()
        cur.close()
        return result
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
