import utils_mongo
import utils_postgres


def run():
    sql = '''select t.id as _id, t.content, a.screen_name, t.happened_at, a.id as account_id, a.name,
     a.followers_count, a.friends_count, a.statuses_count   
    from accounts as a
    join tweets t on a.id = t.author_id
    where (t.compound <= 0.5 and t.compound >= -0.5) and 
    (t.id in ('1246874043682299904', '1246908249577787393', '1247109014694932481') or a.screen_name = 'Marndin12')
    '''
    sql = '''select t.id as _id, t.content, a.screen_name, t.happened_at, a.id as account_id, a.name,
     a.followers_count, a.friends_count, a.statuses_count   
    from accounts as a
    join tweets t on a.id = t.author_id
    where 
    (t.id in ('1246874043682299904', '1246908249577787393', '1247109014694932481'))
    '''

    tweets_cache = {}
    tweets = utils_postgres.exec_sql(sql)
    print(f'tweets count: {len(tweets)}')
    for tweet in tweets:
        hastagas_list = []
        hastagas = utils_postgres.get_hastags_for_tweet(tweet['_id'])
        for h in hastagas:
            hastagas_list.append(h['value'])
        doc = dict(tweet) | {'hastagas': hastagas_list}
        tweets_cache[tweet['_id']] = doc

    for tweet in tweets_cache:
        retweets_raw = utils_postgres.get_retweets_for_tweet(tweet)
        retweet = {}
        for retweet_item in retweets_raw:
            try:
                retweet[retweet_item['id']] = tweets_cache[retweet_item['id']]

            except:
                pass
        doc = tweets_cache[tweet] | {'retweets': retweet}
        utils_mongo.insert_one('embedding', doc)


if __name__ == "__main__":
    run()
