# the intent of this file is to download all images displayed on a webpage and store it within a directory

#heavily used this toutorial: https://www.youtube.com/watch?v=stIxEKR7o-c

import requests
from bs4 import BeautifulSoup
import os

"""
url is the link we are pulling images down from
folder is the name of the folder we are creating (Currently part of code is commented out)
intial_count is the number that we are appending at the end of image 
final_dir is how one selects which inventory to populate with images (barbarekka, thrifty_threads)
"""
def imagedown(url, folder, intial_count, final_dir):
    """try: #  commented out code is the directory creation proccess
        os.mkdir(os.path.join(os.getcwd(), folder))  # creating a folder in the main directory
    except:
        pass  # continues on the program if creation failed, will be pasting all of the images into"""

    dir_path = "D:\IntellijProjects\P5-Tacos-thrift-store\env\static\images" + "\\" + final_dir #only configured for Colin's Machine
    print(dir_path) #  this is the path that we will be creating images in
    os.chdir(dir_path) #  This changes the directory to the folder location on Colin's Machine

    r = requests.get(url) #  passing in the url that was identified in the function
    soup = BeautifulSoup(r.text, 'html.parser')  # looking for specific tag
    images = soup.find_all('img')  # looking for all img tags
    x = intial_count
    for image in images:
        name = 'item' + str(x)  # naming the file item1
        link = image['src']  # getting the formatting with the src tag
        with open(name.replace(' ', '-').replace('/', '') + '.jpg', 'wb') as f:
            im = requests.get(link)
            f.write(im.content)
            print('Writing: ', name)  # communicating back the the user
        x = x + 1 #  itterates up one to get the


print("This is the image downloader")
url = 'https://www.etsy.com/market/vintage_t_shirt' #  note this is the link that we are getting images from

folder_name = 'T-Shirts'
print('this is the link we are scraping from ' + url)
#  print('This is the folder we will be creating ' + folder_name)
imagedown(url, folder_name, 3, 'barbarella')
