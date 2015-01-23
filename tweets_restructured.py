#Format and create a database from a csv file with the following characteristics:
# You’re given a CSV of Twitter’s user activity logs:

# Timestamp,User,Action, Target User
# Wed Sep  3 05:15:39 CDT 2011,143248659,Retweet,55121922
# Thu Sep  4 13:13:33 CDT 2011,143248659,Retweet,189474615
# Sun Sep  7 14:23:36 CDT 2011,65165115,Mention,143248659
# Mon Sep  8 01:39:08 CDT 2011,65165115,Retweet,236403070
# Tue Sep  9 17:59:26 CDT 2011,143248659,Retweet,65165115
# Wed Sep 10 18:57:31 CDT 2011,65165115,Retweet,257366925
# Fri Sep 12 22:52:33 CDT 2011,65165115,Retweet,55121922
# Thu Sep 18 04:34:04 CDT 2011,143248659,Retweet,65165115
# Thu Sep 18 23:10:32 CDT 2011,65165115,Mention,230627444
# Sat Sep 20 18:49:28 CDT 2011,65165115,Reply,310962238

# Actions can be:

# Mention
# Reply
# Retweet

# Produce a table containing, for each user and for each Sun 00:00:00 CDT (that’s the midnight of a Saturday), from the earliest to the latest Sunday present in the dataset, a rolled-up summary of their activity over various time windows ending that midnight.  The columns should be:

# User
# Timestamp (should always be a Sun 00:00:00 CDT)
# # Mentions of Others in Past 7 Days
# # Mentions of Others in Past 31 Days
# # Replies in Past 7 Days
# # Replies in Past 31 Days
# # Retweets in Past 7 Days
# # Retweets in Past 31 Days
# Ratio of # Distinct Target Users to # Actions in Past 31 Days (0 if no actions)

# So the above table should be transformed into:

# 65165115,Sun Sep  7 00:00:00 CDT 2011,0,0,0,0,0,0,0
# 65165115,Sun Sep 14 00:00:00 CDT 2011,1,1,0,0,3,3,1.0
# 65165115,Sun Sep 21 00:00:00 CDT 2011,1,2,1,1,0,3,1.0
# 143248659,Sun Sep  7 00:00:00 CDT 2011,0,0,0,0,2,2,1.0
# 143248659,Sun Sep 14 00:00:00 CDT 2011,0,0,0,0,1,3,1.0
# 143248659,Sun Sep 21 00:00:00 CDT 2011,0,0,0,0,1,4,0.75

#my currently non-working solution
import sqlite3
# import datetime
#from datetime import timedelta
CONN = None
DB = None

def insert_week_actions(user_tweets):

    #input a user's week's data into database 
    query = """INSERT into User_Tweets values (?, ?, ?, ?. ?, ?, ?, ?, ?)"""

    User_id = user_tweets.keys()[0]
    Time = user_tweets[user_id]['date'] 
    Mentions_of_Others_in_Past_7_Days = user_tweets[user_id]['mentions']
    Mentions_of_Others_in_Past_31_Days = 0
    Replies_in_Past_7_Days = user_tweets[user_id]['replies']
    Replies_in_Past_31_Days = 0
    Retweets_in_Past_7_Days = user_tweets[user_id]['retweets']
    Retweets_in_Past_31_Days = 0
    Ratio_Target_Users_to_Actions = 0

    DB.execute(query, (User_id, Time, Mentions_of_Others_in_Past_7_Days, Mentions_of_Others_in_Past_31_Days, Replies_in_Past_7_Days, Replies_in_Past_31_Days, Retweets_in_Past_7_Days, Retweets_in_Past_31_Days, Ratio_Target_Users_to_Actions))

    CONN.commit()


def count_and_insert_week_actions(filename):

    f = open(filename)

    user_tweets = {}
    dates = []

    for line in f:
        tweet = line.rstrip().split(',')
        #need to convert current date into manageable ints that represent 7 days for subtraction, probably using datetime or timedelta. So confusing, will figure out later...
        current_date = tweet[0][4:10]
        dates.append(current_date)
        user_id = tweet[1]

        if current_date - dates[0] < 7 and user_id == user_tweets[user_id]:
            
            # if key is already in dict, update counts for actions
            if user_tweets.get(user_id, False) != False:

                if tweet[2] == 'Mention':
                    user_tweets[user_id]['mentions'] += 1

                elif tweet[2] == 'Reply':
                    user_tweets[user_id]['replies'] += 1

                elif tweet[2] == 'Retweet':
                    user_tweets[user_id]['retweets'] += 1

                #get last date in week
                user_tweets[user_id]['date'] = tweet[4:28]

            # if key is not there, input userID as key and initialize counts
            else: 
                user_tweets[user_id = {'date': '', 'mentions': 0 , 'replies': 0, 'retweets': 0}

        #what the user_tweets dict looks like now:
        # {143248659: {date: "Sun Sep  7 14:23:36 CDT 2011", 'mentions': 14, 'replies': 3, 'retweets': 4}}

            
        insert_week_actions(user_tweets)
    #oops: the values of the counts will get overwritten for every 7 day period, so at this point, I'll only be inputting one row into the database, with the values of the very last iteration of the whole csv file.
    # BUT, if I indent the function call, I'll be inserting into the database for every iteration of each line, which is ridiculous and very inefficient. 

    f.close()


def connect_to_db():
    global DB, CONN
    CONN = sqlite3.connect("tweets.db")
    DB = CONN.cursor()

def main():
    connect_to_db()
    count_and_insert_week_actions('tweets.csv')

    #create table - run file first time, commented out so as not to create table every time file is run
    # DB.execute('''CREATE TABLE User_Tweets
    #              (User_id INT, Time text, Mentions_of_Others_in_Past_7_Days INT, Mentions_of_Others_in_Past_31_Days INT, Replies_in_Past_7_Days INT, Replies_in_Past_31_Days INT, Retweets_in_Past_7_Days INT, Retweets_in_Past_31_Days INT, Ratio_Target_Users_to_Actions INT)''')

    # CONN.commit()

    CONN.close()

if __name__ == "__main__":
    main()

#Issues:
#still need to solve how to calculate a rolling count for the 31 day column value, as well as calculating the ratio of distinct target users to actions. 
#Also, dates don't start on Sat, but start at first tweet of a user and then calculate to the next 7 days. 
