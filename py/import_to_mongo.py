from bson import ObjectId

import utils_mongo
import utils_postgres


def migrate_account(account_id):
    sql = f'select * from accounts where id = \'{account_id}\''
    acc = utils_postgres.exec_sql(sql)[0]
    return utils_mongo.insert_one('accounts', dict(acc))

def migrate_tweet(tweet):
    global account_cache
    global tweets_cache
    if tweet['account_id'] not in account_cache:
        account_cache[tweet['account_id']] = migrate_account(tweet['account_id'])

    hastagas_list = []
    hastagas = utils_postgres.get_hastags_for_tweet(tweet['id'])
    for h in hastagas:
        hastagas_list.append(h['value'])
    doc = dict(tweet) | \
          {'hastagas': hastagas_list,
           'account_id': ObjectId(account_cache[tweet['account_id']].inserted_id)}
    tweets_cache[tweet['id']] = utils_mongo.insert_one('tweets', doc)

def run():
    sql = '''select t.id, t.content, t.happened_at, t.parent_id, t.author_id as account_id
    from tweets t 
    where     (t.compound <= 0.5 and t.compound >= -0.5) and
     (t.author_id = '3003720760')
    '''




    tweets = utils_postgres.exec_sql(sql)
    print(f'tweets count: {len(tweets)}')

    for tweet in tweets:
       migrate_tweet(tweet)


account_cache = {}
tweets_cache = {}
if __name__ == "__main__":
    run()
