import requests
import json
import os

'''**TO WORK**makes a temp directory to store images.  Right now using actual directory--mkdtemp will be true temp'''
#t.mkdtemp(prefix='images') comment out until figure out temp directory usage

'''This determines the latest xkcd cartoon to create the for loop to cover all'''
latest_comic = 'https://xkcd.com/info.0.json'
temp = requests.get(latest_comic)
temp_data = temp.json()
last_comic_number = int(temp_data['num'])


#iterate over comics
#iterate over comics  **NEED TO CHANGE to cover full range**
for x in range(200, 210):
    website = 'https://xkcd.com/' + str(x) + '/info.0.json'
    response = requests.get(website)
    if response.status_code == requests.codes.ok:  #checks to see if a valid site--gets over the 404 problem

        data = response.json()
        
        #saves file
        filename = str(x) +'.png'
        r = requests.get(data['img'])

        with open(filename, 'wb')as f:
            f.write(r.content) 

