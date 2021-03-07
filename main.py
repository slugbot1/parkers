from datetime import datetime

import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("BdP6cTqm4iBm7H6nOfVtQzd3D",
    "aZ3sB7PHhudGotPLuHxFMqSyXEnh75eSUrcwkqkhujyvvhl686")
auth.set_access_token("1368231774669705219-ve9Hied8L8J6E4vbrSLCyFhVw28ZRT",
    "MWwZZXWlmKnybLjO90osaaNZO86OF69Urqm4xhfGe8ili")

api = tweepy.API(auth)

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)

#timeline = api.home_timeline()
#for tweet in timeline:
#    print(f"{tweet.user.name} said {tweet.text}")

dateTimeObj = datetime.now()
timestampStr = dateTimeObj.strftime("%d-%b-%Y (%H:%M:%S.%f)")

api.update_status("No. \n"
                      "\n\n\n\n\n\n\n\n\n"
                      "#Celtic @CelticFC #SPL #GoingFor52 \n"
                      "#COVID19 #SNP @NicolaSturgeon \n"
                      "TweetID: 1967-" + timestampStr)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")


