import requests
from zipfile import ZipFile
url = 'https://github.com/Kaifungamedev/save-load-in-python/archive/refs/heads/main.zip' # original link is broken
r = requests.get(url, allow_redirects=True)
zipName = 'file'
open(zipName + '.zip', 'wb').write(r.content)

with ZipFile(f'{zipName}.zip', 'r') as f:
    f.extractall(zipName)

