import requests, os, webbrowser, bs4
import urllib.request
import ctypes
import datetime
import time
from apscheduler.scheduler import Scheduler
import re


def downloadimage():
    # Download archdaily's general projects page
    res = requests.get('http://www.archdaily.com/search/projects')
    res.raise_for_status

    # Parse the page to find the first project
    site = bs4.BeautifulSoup(res.text, "html.parser")
    project_link = site.find('ul',{'class':'afd-search-list'})
    one = project_link.find('a',href=True)
    two = one['href']

    
    res2 = requests.get('http://www.archdaily.com' + two)
    res2.raise_for_status

    site_project = bs4.BeautifulSoup(res2.text, "html.parser")
    image_link = site_project.find('div',{'class':'image-bookmark'})
    image_car = image_link.find('a',href=True)
    image_car = image_car['href']

    res3 = requests.get(image_car)
    res3.raise_for_status

    site_project = bs4.BeautifulSoup(res2.text, "html.parser")
    image_link = site_project.find('div',{'class':'image-bookmark'})

    # try:
    #     image = re.search('data-image="(.+?)"', str(image_link)).group(1)
    # except AttributeError:
    #     image = 'Sorry dunno what happened'

    # data = urllib.request.urlretrieve((image), 'C:/Users/jason/Desktop/test.jpg')

    print (image_car)

    # # first project's page extension
    # project_link_ref = project_link[0].get('href')

    # # Download the projects page
    # res2 = requests.get(project_link_ref)
    # res2.raise_for_status

    # # Parse the page and find the image
    # devart_image = bs4.BeautifulSoup(res2.text)
    # image_link = devart_image.select('div.dev-view-main-content img')
    # image = image_link[0].get('src')

    # # Download image
    # data = urllib.request.urlretrieve((image), 'C:/Users/jason/Desktop/background/001.jpg')
    

downloadimage()

# def setbackground():
#     # Set image as background
#     SPI_SETDESKWALLPAPER = 0x14
#     SPIF_UPDATEINFILE = 0x2
#     src = 'C:/Users/jason/Desktop/background/001.jpg'

#     print(ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, src, SPIF_UPDATEINFILE))
    



# def interval():
#     downloadimage()
#     setbackground()
#     print(datetime.datetime.now())
#     time.sleep(20)
    
#     return

    

# sched = Scheduler()
# sched.daemonic = False
# sched.start()   

# sched.add_cron_job(interval, minute='0-59')