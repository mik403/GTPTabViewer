__author__ = 'Michael'

import sys
#sys.platform = 'linux2'

import os.path
import requests

def download_file(self, url):
    save_dir = self.user_data_dir
    local_filename = url.split('/')[-1]
    local_file = os.path.join(save_dir, local_filename + ".gp3")
    response = requests.get(url, stream=True)
    with open(local_file, 'wb') as f:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
                f.flush()
    return local_file

def download_tab(self):
    #url = "https://www.google.com.ua/images/nav_logo242.png"
    url = "http://www.gtp-tabs.ru/n/tabs/download/2273.html"
    path = download_file(self, url)
    return path


