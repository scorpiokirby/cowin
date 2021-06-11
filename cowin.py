import requests
import time
from time import sleep
#from playsound import playsound

stateid = 10
distid = 152
date = '11-06-2021'
age = 18
url = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id={}&date={}'.format(distid,date)

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}

def findslot():
    counter = 0
    urlresult = requests.get(url,headers=header)
    resultjson = urlresult.json()
    data = resultjson["sessions"]

    for eachrow in data:
        if((eachrow["available_capacity"] > 0) & (eachrow["min_age_limit"] == age)):
            counter = counter+1
            print (eachrow["name"])
            print (eachrow["address"])
            print (eachrow["block_name"])
            print (eachrow["vaccine"])
            #playsound('python/ding-sound.mp3')
            return True

    if (counter == 0):
        print ("No Vaccine Slots Available for Now!!!")
        return False

while (findslot() == False):
    sleep(5)
    findslot()




