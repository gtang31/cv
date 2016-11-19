import os
import requests

KEY = os.environ["PEXEL_API_KEY"]
headers = {"Authorization": KEY}
url = "http://api.pexels.com/v1/search?query=dog&per_page=250&page=1"
r = requests.get(url, headers=headers)

