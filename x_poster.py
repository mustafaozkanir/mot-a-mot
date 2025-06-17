import os
import tweepy

from dotenv import load_dotenv
from date_generator import generate_date
# Load credentials from .env file
load_dotenv()

# API credentials (OAuth 1.0a User Context)
consumer_key = os.getenv("API_KEY")
consumer_secret = os.getenv("API_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_secret = os.getenv("ACCESS_SECRET")

# Authenticate using Tweepy Client (v2)
client = tweepy.Client(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_secret
)

def post_to_twitter(text):
    try:
        response = client.create_tweet(text=text)
        print("✅ Tweet posted successfully!")
        print("Tweet ID:", response.data.get("id"))
    except Exception as e:
        print("❌ Error posting tweet:", e)

if __name__ == "__main__":

    tweet_text = "🗓️  𝐓𝐨𝐝𝐚𝐲'𝐬 𝐃𝐚𝐭𝐞 𝐢𝐧 𝐅𝐫𝐞𝐧𝐜𝐡: \n" + generate_date("french") + "\n" + generate_date("english")
    print(tweet_text)
    
    post_to_twitter(tweet_text)
