import warnings
warnings.filterwarnings("ignore")
import requests
import shutil
import os
import sys
from pathlib import Path
home = Path.home()
script = Path(__file__).resolve()
destination = f"{home}/QuoteFolder"
if not os.path.exists(destination):
    os.makedirs(destination)

if not str(script.parent) == destination:
    shutil.move(str(script), str(destination))
    sys.exit()
    


URL = 'https://api.quotable.io/random'
HEADERS = {
    "Content-Type": "application/json; charset=utf-8"
}
response = requests.get(URL, headers= HEADERS, verify=False)
quote = response.json()["content"]
author = response.json()["author"]

print("Quote: "+ '"' + quote + '"' + " Author: " + author)
