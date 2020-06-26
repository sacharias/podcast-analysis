import feedparser
import requests

# rss_feed = "joeroganexp.joerogan.libsynpro.com/rss"
rss_source = "./joerogan-rss"

d = feedparser.parse(rss_source)

print(d.keys())

# print(d['feed']['title'])

# last episode
last_episode = d['entries'][0]
audio_link = last_episode['link']

# download
r = requests.get(audio_link, allow_redirects=True)
open('audio/joerogan1.mp3', 'wb').write(r.content)