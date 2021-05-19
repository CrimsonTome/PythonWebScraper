import requests 
from bs4 import BeautifulSoup
from time import sleep
import urlname
    
def getdata(url): 
    r = requests.get(url) 
    return r.text 
    
htmldata = getdata(urlname.url) 
soupData = BeautifulSoup(htmldata, 'html.parser')
listofimages = []
count = 1
for item in soupData.find_all('img'):
    listofimages.append(item['src'])
for i in listofimages:
    try:
        print (i)
        response = requests.get(i)

        file = open("image"+str(count)+".png", "wb")
        file.write(response.content)
        file.close()
        count+=1
        print("download of "+i+" complete \n")
        sleep(1)
    except:
        print("Sorry, something went wrong. Moving onto the next image \n")
    


