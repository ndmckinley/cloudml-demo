import reddit
import urllib
import os

for subreddit in ['aww', 'cats', 'puppysmiles', 'tinyanimalsonfingers', 'beachdogs', 'kitty', 'happydogs']:
  p = []
  after = None
  for _ in range(20):
    print subreddit, _
    posts, after = reddit.get_hot(subreddit, after=after)
    p += reddit.get_previews(posts)
  for idx, url in enumerate(p):
    urllib.urlretrieve(url, os.path.join(".", "data", subreddit, "%d.jpg" % idx))
