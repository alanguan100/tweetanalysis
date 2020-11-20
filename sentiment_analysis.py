# CS1026 - Assignment 3 - Sentiment Analysis
# Name: Alan Guan
# SN: 251142944

#lists for storing happiness value by region
eastern_region = 0
central_region = 0
mountain_region = 0
pacific_region = 0

pacific_tweetTotal = 0
pacific_keywordTweets = 0

def compute_tweets(tweet, keyword):
#variables to store final values in by region
    pacific_tweetTotal = 0
    pacific_keywordTweets = 0
    pacific_Sentiment = 0

    mountain_tweetTotal = 0
    mountain_keywordTweets = 0
    mountain_Sentiment = 0

    central_tweetTotal = 0
    central_keywordTweets = 0
    central_Sentiment = 0

    eastern_tweetTotal = 0
    eastern_keywordTweets = 0
    eastern_Sentiment = 0

    try: #opens tweet and keyword file
        tweetsListed = open(tweet, "r", encoding="utf+8").read().split("\n") #opens tweet file given by user, reads and splits it
        keywords = open(keyword, "r").read() # opens and reads keyword file given by user
        keywordArray = keyword_computationSort(keywords) #calls keyword parsing function and stores in variable
        tweetsArray = []
        for tweet in tweetsListed:      # parses and organizes tweet file
            tweetStripped = tweet_computationSort(tweet)
            tweetsArray.append(tweetStripped)

        for tweet in tweetsArray: #loop that goes until all tweets are analyzed
            timezone_computation(tweet) #computing what timezone tweet is in
            tweetScore = sentiment_computation(tweet,keywordArray)
            tweet.insert(0,tweetScore)

        for i in tweetsArray:   #loop to calculate total tweets, keyword tweets, and sentiment by region
            if i[1] == "pacific":
                if i[0] == 0:
                    pacific_tweetTotal += 1
                else:
                    pacific_tweetTotal +=1
                    pacific_keywordTweets += 1
                    pacific_Sentiment += float(i[0]) #float as average can contain decimals
            if i[1] == "mountain":
                if i[0] == 0:
                    mountain_tweetTotal += 1
                else:
                    mountain_tweetTotal +=1
                    mountain_keywordTweets += 1
                    mountain_Sentiment += float(i[0])
            if i[1] == "central":
                if i[0] == 0:
                    central_tweetTotal += 1
                else:
                    central_tweetTotal +=1
                    central_keywordTweets += 1
                    central_Sentiment += float(i[0])
            if i[1] == "eastern":
                if i[0] == 0:
                    eastern_tweetTotal += 1
                else:
                    eastern_tweetTotal +=1
                    eastern_keywordTweets += 1
                    eastern_Sentiment += float(i[0])

        if pacific_keywordTweets == 0:  # loop to tally up final scores
            pacificScore = 0
        else:
            pacificScore = pacific_Sentiment/pacific_keywordTweets # calculation of final score (average)
        pacificFinal = (pacificScore, pacific_keywordTweets, pacific_tweetTotal)

        if mountain_keywordTweets == 0:
            mountainScore = 0
        else:
            mountainScore = mountain_Sentiment/mountain_keywordTweets
        mountainFinal = (mountainScore, mountain_keywordTweets, mountain_tweetTotal)

        if central_keywordTweets == 0:
            centralScore = 0
        else:
            centralScore = central_Sentiment/central_keywordTweets
        centralFinal = (centralScore, central_keywordTweets, central_tweetTotal)

        if eastern_keywordTweets == 0:
            easternScore = 0
        else:
            easternScore = eastern_Sentiment/eastern_keywordTweets
        easternFinal = (easternScore,eastern_keywordTweets,eastern_tweetTotal)

        allScores = [easternFinal,mountainFinal,centralFinal,pacificFinal] # final tuple output
        return allScores

    except IOError: # input/output error used as data validation for user file name input
        print('Invalid Input File')
        allScores = []
        return allScores # returns a blank list if incorrect file names are entered


#function to clean up tweet file
def tweet_computationSort(tweet):
    updatedTweet = []
    singleTweet = tweet.split(" ")
    for word in singleTweet:
        try:
            if word.strip("][-")[0].isdigit():
                strippedWord = word.strip("!@#$%^&*()_+=~`{}|[]\\|\'\";:,./<>?").lower() #convert to lowercase and get rid of punctuation
                updatedTweet.append(strippedWord)
            else:
                strippedWord = word.strip("!@#$%^&*()_+=~`{}|[]\\|\'\";:,./<>?").lower()
                updatedTweet.append(strippedWord)
        except:
            pass
    #print(updatedTweet)
    return updatedTweet # compiles all tweets into one long line for easy analysis

def keyword_computationSort(keywords):  # function to split and make keyword file into list
    keywordArray = []
    keywordPairs = keywords.split("\n")
    for i in keywordPairs:
        c = i.split(",")
        keywordArray.append(c)
    return keywordArray


def timezone_computation(tweet): # timezone function
    try:
        lat = float(tweet[0])
        long = float(tweet[1])
    except:
        lat =0
        long=0
    if 49.189787 >= lat >= 24.660845:   #calculation to determine which timezone tweet falls in
        if - 67.444574 >= long >= -87.518395:
            tweet.insert(0, "eastern")
        elif -87.518395 > long >= -101.998892:
            tweet.insert(0, "central")
        elif -101.998892 > long >= -115.236428:
            tweet.insert(0, "mountain")
        elif -115.236428 > long >= -125.242264:
            tweet.insert(0, "pacific")
        else:
            tweet.insert(0, "none")
    else:
        tweet.insert(0, "none")
    return tweet


def sentiment_computation(tweet,keyword): #sentiment analysis function
    total_sentiment = 0
    keywordCount = 0
    keyword = [x for x in keyword if x != ['']] #in place to prevent indexing errors by removing empty lists
    for word in tweet:
        for key in keyword:
            if word == key[0]:
                total_sentiment += int(key[1]) #sentiment counter adding the values at index 1
                keywordCount += 1 #total keyword counter
            else:
                pass
    if keywordCount == 0:
        return 0
    else:
        sentimentValue = total_sentiment/keywordCount #average calcualtion
        return sentimentValue






