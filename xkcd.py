 import requests
import json
import tempfile as t
import os
import shutil

'''**TO WORK**makes a temp directory to store images.  Right now using actual directory--mkdtemp will be true temp'''
#t.mkdtemp(prefix='images') comment out until figure out temp directory usage

os.mkdir('images')


'''This determines the latest xkcd cartoon to create the for loop to cover all'''
latest_comic = 'https://xkcd.com/info.0.json'
temp = requests.get(latest_comic)
temp_data = temp.json()
last_comic_number = int(temp_data['num'])

#iterate over comics
for x in range(400, 410):
    website = 'https://xkcd.com/' + str(x) + '/info.0.json'
    response = requests.get(website)
    if response.status_code == requests.codes.ok:  #checks to see if a valid site--gets over the 404 problem

        data = response.json()
        
        #gets rid of special characters title name to prevent save errors
        alphanumeric = ""
        for character in data['safe_title']:
            if character.isalnum():
                alphanumeric += character
        
        #saves file
        filename = 'images/' + str(x) + '_' + alphanumeric +'.png'
        r = requests.get(data['img'])

        with open(filename, 'wb')as f:
            f.write(r.content) 
     
        '''this writes alt text to text file, with line numbered by comic'''
        hover_text = data['alt']
        number = data['num']

        with open("images/alt-text.txt", 'a')as f:
            f.write(str(number) + ': ' + hover_text + "\n")
            f.write("\n")
            
'''**TO WORK** Create a document'''


"""**TO WORK iterate over pictures and alt-text and insert into doc; """
'''deletes directory used to store images during process'''  
shutil.rmtree('images')
