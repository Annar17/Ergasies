import twitter
import re
import collections
import itertools

api = twitter.Api(consumer_key='FILL_THIS',
                  consumer_secret='FILL_THIS',
                  access_token_key='FILL_THIS',
                  access_token_secret='FILL_THIS')
print(api.VerifyCredentials())
print('\n')

username = input('Please write your username:')
tweets = api.GetUserTimeline(screen_name=username, count=10)
print('\n')

tweetslist = []
print('Your last 10 tweets are:')
for t in tweets[:10]:
    mystr = t.text
    tweetslist.append(re.sub("[^\w]", " ", mystr).split())
    print(t.text)

print('\n')
words = list(itertools.chain.from_iterable(tweetslist))

counter = collections.Counter(words)
print('The most used word in your last 10 tweets is', counter.most_common(1))
