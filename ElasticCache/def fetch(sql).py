def fetch(sql):
    ttl = 10 #cached results last for 10 seconds
    try:
        params = config(section='redis')
        cache = redis.Redis.from_url(params['redis_url'])
        retval = cache.get(sql)
        if (retval != None):
            return retval.decode()
        else:
            # connect to database listed in database.ini
            conn = connect()
            if(conn != None):
                cur = conn.cursor()
                cur.execute(sql)

                # fetch one row
                retval = cur.fetchone()

                # close db connection
                cur.close() 
                conn.close()
                print("PostgreSQL connection is now closed")

                # cache result
                cache.setex(sql, ttl, ''.join(retval))
                return retval
            else:
                return None
    except redis.RedisError:
        logger.error('Error connecting to Redis')
