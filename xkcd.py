import requests
import json
import tempfile as t
import os
import shutil
import aspose.words as aw

'''**TO WORK**makes a temp directory to store images.  Right now using actual directory--mkdtemp will be true temp'''
#t.mkdtemp(prefix='images') comment out until figure out temp directory usage

os.mkdir('images')


'''This determines the latest xkcd cartoon to create the for loop to cover all'''
latest_comic = 'https://xkcd.com/info.0.json'
temp = requests.get(latest_comic)
temp_data = temp.json()
last_comic_number = int(temp_data['num'])

'''**TO WORK** Create a blank document'''
# create document object
doc = aw.Document()

# create a document builder object
builder = aw.DocumentBuilder(doc)


#iterate over comics
#iterate over comics  **NEED TO CHANGE to cover full range**
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

        # add image into document
        #imageName = "images/" + "409_ElectricSkateboardDoubleComic.png"
        builder.insert_image(filename)  

        """insert hovertext below image"""
        # create font
        font = builder.font
        font.size = 16
        font.bold = True
        font.name = "Arial"
        #font.underline = aw.Underline.DASH

        # set paragraph formatting
        paragraphFormat = builder.paragraph_format
        paragraphFormat.first_line_indent = 8
        paragraphFormat.alignment = aw.ParagraphAlignment.JUSTIFY
        paragraphFormat.keep_together = True

        # add text
        builder.writeln(data['alt'])  
     
        '''**NEED TO WORK INTO DOC)this writes alt text to text file, with line numbered by comic'''
        hover_text = data['alt']
        number = data['num']


        with open("images/alt-text.txt", 'a')as f:  #if printing in book this can be skipped
            f.write(str(number) + ': ' + hover_text + "\n")
            f.write("\n")
      




# save document
doc.save("out.docx")
'''deletes directory used to store images during process'''  
shutil.rmtree('images')
