import os, time, sys
from tqdm import tqdm
from flickrapi import FlickrAPI
from urllib.request import urlretrieve

key = '8b7527f3a284febb4979359135742a89'
secret = '8a7cae070e75be36'
wait_time = 1

keyword = sys.argv[1]
savedir = './' + keyword

flickr = FlickrAPI(key, secret, format='parsed-json')

result = flickr.photos.search(
  text = keyword,
  per_page = 330,
  media = 'photos',
  sort = 'relevance',
  safe_search = 1,
  extras = 'url_q, license'
)

photos = result['photos']

for i, photo in tqdm(enumerate(photos['photo'])):
  url_q = photo['url_q']
  filepath = savedir + '/' + photo['id'] + '.jpg'
  if os.path.exists(filepath): continue
  urlretrieve(url_q, filepath)
  time.sleep(wait_time)