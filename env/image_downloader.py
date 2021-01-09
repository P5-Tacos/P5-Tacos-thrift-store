# the intent of this file is to download all images displayed on amazon

#heavily used this toutorial: https://www.youtube.com/watch?v=stIxEKR7o-c

import requests
from bs4 import BeautifulSoup
import os


def imagedown(url, folder):
    try:
        os.mkdir(os.path.join(os.getcwd(), folder))  # creating a folder in the main directory
    except:
        pass  # continues on the program if creation failed, will be pasting all of the images into

    parent_dir = "D:\IntellijProjects\P5-Tacos-thrift-store\env\static\images"  #  this is the directory that the static images are at
    path = os.path.join(parent_dir, folder)
    os.mkdir(path)
    #  os.chdir(os.path.join(os.getcwd(), folder))  # creating a folder based off of name provided

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')  # looking for specific tag
    images = soup.find_all('img')  # looking for all img tags
    x = 50
    for image in images:
        name = 'item' + str(x)  # naming the file item1
        link = image['src']  # getting the formatting with the src tag
        with open(name.replace(' ', '-').replace('/', '') + '.jpg', 'wb') as f:
            im = requests.get(link)
            f.write(im.content)
            print('Writing: ', name)  # communicating back the the user
        x = x + 1


print("This is the image downloader")
url = 'https://www.etsy.com/market/vintage_t_shirt'

folder_name = 'T-Shirts'
print('this is the link we are scraping from ' + url)
print('This is the folder we will be creating ' + folder_name)
imagedown(url, folder_name)
