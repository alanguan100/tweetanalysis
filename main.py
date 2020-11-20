#Alan Guan Code

from sentiment_analysis import *
#program inputs
keyword = input("Please enter name of file with Tweet Keywords: ") #keywords with list of words and respective sentiment
tweet = input("Please enter name of file with tweets: ")

# variable to store tweet computation output
final_result = compute_tweets(tweet, keyword)
# Region level output of avg happiness sentiment, total tweets, and number of tweets containing keywords

if final_result == []:
    print(final_result)
else:
    print("Eastern Region: ")
    print("     Average happiness sentiment is:", final_result[0][0])
    print("     Number of keyword tweets is:", final_result[0][1])
    print("     Number of tweets is:", final_result[0][2])
    print()
    print("Central Region: ")
    print("     Average happiness sentiment is:", final_result[2][0])
    print("     Number of keyword tweets is:", final_result[2][1])
    print("     Number of tweets is:", final_result[2][2])
    print()
    print("Mountain Region: ")
    print("     Average happiness sentiment is:", final_result[1][0])
    print("     Number of keyword tweets is:", final_result[1][1])
    print("     Number of tweets is:", final_result[1][2])
    print()
    print("Pacific Region: ")
    print("     Average happiness sentiment is:", final_result[3][0])
    print("     Number of keyword tweets is:", final_result[3][1])
    print("     Number of tweets is:", final_result[3][2])

