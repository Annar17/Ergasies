import twitter
import re
import collections
import itertools

api = twitter.Api(consumer_key='F17yaTczDvqBgAfWS7VUwYFyk',
                  consumer_secret='OsSYni1hLYaXyd0lJbHcNApQhVIuBBQ3u0VOfyXQtzxGbAkfGz',
                  access_token_key='954404620117446658-cKVtCnUCwuIYnlp25bG4RkGCiagQIRz',
                  access_token_secret='LVKWMgs8TmugydytCxJOLkoSPqWEIcx8V2qshbvVizGTQ')
print(api.VerifyCredentials())
print('\n')

username = input("Dwste to username sas:")
tweets = api.GetUserTimeline(screen_name=username, count=10)
print('\n')

tweetslist = []
print('Your last 10 tweets are:')
for t in tweets[:10]:
    mystr = t.text
    tweetslist.append(re.sub("[^\w]", " ",  mystr).split())
    print(t.text)

print('\n')
words = list(itertools.chain.from_iterable(tweetslist))

counter = collections.Counter(words)
print('The most used word in your last 10 tweets is',counter.most_common(1))

