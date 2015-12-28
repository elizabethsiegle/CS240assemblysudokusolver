# Any line that begins with a hash (pound sign) is ignored by the program
# Like this one
# These are called comments
# Think of comments in code as marginalia

# This Is Just To Say
# William Carlos Williams, 1883 - 1963
#
# I have eaten
# the plums
# that were in
# the icebox
#
# and which
# you were probably
# saving
# for breakfast
#
# Forgive me
# they were delicious
# so sweet
# and so cold



# First we need to import helper libraries--or modules--into our program
# Using existing modules saves us from writing code that someone already has developed
# (Why invent the wheel when you can borrow one?)

# So below we're importing several modules
from wordnik import * 
import tweepy #hooks into twitter api
import inflect 

# Next we need to set up APIs--ways to communicate with external services or data
apiUrl = 'http://api.wordnik.com/v4'
apiKey = 'QVUUlqbJ6ITiXKhPSS7c4JB3LTcYnTw44EqzQZoc7HSBfYEU22'

auth = tweepy.OAuthHandler("consumerkey", "consumersecret")
auth.set_access_token('oauthtoken', 'oauthsecret')

# Set up abbreviations so we don't have to refer to the full name of the helper library or API every time
client = swagger.ApiClient(apiKey, apiUrl)
wordApi = WordsApi.WordsApi(client)
api = tweepy.API(auth)
p = inflect.engine()

# Let's generate a poem!
nouns = wordApi.getRandomWords(includePartOfSpeech='noun',minCorpusCount=10000,hasDictionaryDef='true',minDictionaryCount=10,limit=2,maxLength=30)
adjectives = wordApi.getRandomWords(includePartOfSpeech='adjective',limit=3,minCorpusCount=100,hasDictionaryDef='true')
plums = nouns[0].word
icebox = nouns[1].word
delicious = adjectives[0].word
sweet = adjectives[1].word
cold = adjectives[2].word
stanzaOne = "I have eaten\nthe " + p.plural(plums) + "\nthat were in\nthe " + icebox + "\n"
stanzaTwo = "\nForgive me\nThey were " + delicious + "\nso " + sweet + "\nand so " + cold

# What do you think the \n does? -->space

poem = stanzaOne + stanzaTwo
print poem

# Let's send the poem to Twitter
#api.update_status(poem)