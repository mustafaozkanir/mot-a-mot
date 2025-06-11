import os
import tweepy
from dotenv import load_dotenv

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
    # Load post content from file (or use your own string)
    try:
        with open("latest_post.txt", "r", encoding="utf-8") as f:
            tweet_text = f.read().strip()
    except FileNotFoundError:
        tweet_text = "Bonjour ! Ceci est un tweet automatique. 🇫🇷"

    """
    if len(tweet_text) > 280:
        tweet_text = tweet_text[:277] + "..."
        print("⚠️ Tweet was too long. Truncated to 280 characters.")
    """
    
    post_to_twitter(tweet_text)
