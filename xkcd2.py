import requests
import os
import time
import concurrent.futures
from PIL import Image


num_threads = 8
start = time.time()

content = {}

def checkComics(number):
    website = 'https://xkcd.com/' + str(number) + '/info.0.json'
    response = requests.get(website)
    breakpoint()    
    #checks to see if a valid site--gets over the 404 problem
    if response.status_code == requests.codes.ok:  
        # print(f'{number}: OK')
        data = response.json()
        r = requests.get(data['img'])
        filename = 'images/' + str(number) +'.png'
        
        with open(filename, 'wb')as f:
            f.write(r.content)
        img = Image.open(filename)
        width = img.width
        height = img.height
        
#'content' is dictionary containing Title, Alt Text, image width, image height        
        content[str(number)] ={'title': data['safe_title'],
                              'alt_text' : data['alt'],
                              'img_width': width,
                              'img_height': height}
    else: print(f'{number}: FAILED')
    # return response
        
        
def runThread(max_thread, list_to_do):
    with concurrent.futures.ThreadPoolExecutor(max_workers = max_thread) as executor:  
        checkSite = {executor.submit(checkComics, comic): comic for comic in list_to_do}

#make directory to store images:
if not os.path.isdir('images'):
    os.mkdir('images')


'''This determines the latest xkcd cartoon to create the for loop to cover all'''
latest_comic = 'https://xkcd.com/info.0.json'
temp = requests.get(latest_comic)
# temp_data = temp.json()
last_comic_number = int(temp.json()['num'])
list_of_comics = []
for x in range(last_comic_number):
    list_of_comics.append(x+1)


#break total list into 8    
list1 = list_of_comics[:(int(len(list_of_comics)/8))]    
list2 = list_of_comics[(int(len(list_of_comics)/8)):(int(len(list_of_comics)/4))] 
list3 = list_of_comics[(int(len(list_of_comics)/4)):(int(len(list_of_comics)/(8/3)))] 
list4 = list_of_comics[(int(len(list_of_comics)/(8/3))):(int(len(list_of_comics)/2))]  
list5 = list_of_comics[(int(len(list_of_comics)/2)):(int(len(list_of_comics)/(8/5)))]    
list6 = list_of_comics[(int(len(list_of_comics)/(8/5))):(int(len(list_of_comics)/(4/3)))] 
list7 = list_of_comics[(int(len(list_of_comics)/(4/3))):(int(len(list_of_comics)/(8/7)))] 
list8 = list_of_comics[(int(len(list_of_comics)/(8/7))):]   
 

lists = [list1, list2, list3, list4, list5, list6, list7, list8]

with concurrent.futures.ProcessPoolExecutor(max_workers=8) as executor:
    doComics = {executor.submit(runThread,num_threads,alist): alist for alist in lists}    

# with concurrent.futures.ThreadPoolExecutor(max_workers = num_threads) as executor:  
#     checkSite = {executor.submit(checkComics, comic): comic for comic in list_of_comics}
# z= len(list_of_comics) 

# lists = np.array_split(list_of_comics, num_threads)

# bkpts = []
# for a in range(num_threads):
#     bkpts.append(int(z * ( (a+1) / num_threads) ) )
# bkpts = [int(z//4),int(z//2),int(z * 0.75)]

#generate lists
# for thread in range(8):
    
#     check_comic_thread_ + str(thread) = threading.Thread(target=checkComics, args = lists[thread],) 
   
# list1 = list_of_comics[:(bkpts[0])+1]
# list2 = list_of_comics[(bkpts[0]): (bkpts[1])+1]    
# list3 = list_of_comics[(bkpts[1]): (bkpts[2])+1]
# list4 = list_of_comics[(bkpts[2]):]     
print(f'Start at {start}')   
# checkComics(list_of_comics)
# check_comic_thread = threading.Thread(target=checkComics, args=(list1,))
# check_comic_thread2 = threading.Thread(target=checkComics, args=(list2,))
# check_comic_thread3 = threading.Thread(target=checkComics, args=(list3,))
# check_comic_thread4 = threading.Thread(target=checkComics, args=(list4,))

# check_comic_thread.start()
# check_comic_thread2.start()
# check_comic_thread3.start()
# check_comic_thread4.start()

# check_comic_thread.join()
# check_comic_thread2.join()
# check_comic_thread3.join()
# check_comic_thread4.join()
end = time.time()

print(f'DONE. {end-start} seconds. ')
# #iterate over comics
# #iterate over comics  **NEED TO CHANGE to cover full range**
# for x in range(1, last_comic_number+1):
#     website = 'https://xkcd.com/' + str(x) + '/info.0.json'
#     response = requests.get(website)
    
#     #checks to see if a valid site--gets over the 404 problem
#     if response.status_code == requests.codes.ok:  
#         print(f'{x}: OK')
#         data = response.json()
#     else: print(f'{x}: FAILED')
        
        #gets rid of special characters title name to prevent save errors
        # alphanumeric = ""
        # for character in data['safe_title']:
        #     if character.isalnum():
        #         alphanumeric += character
        
        # #saves file
        # filename = 'images/' + str(x)  +'.png'
        # r = requests.get(data['img'])

        # with open(filename, 'wb')as f:
        #     f.write(r.content) 

#         # add image into document
#         #imageName = "images/" + "409_ElectricSkateboardDoubleComic.png"
#         builder.insert_image(filename)  

#         """insert hovertext below image"""
#         # create font
#         font = builder.font
#         font.size = 16
#         font.bold = True
#         font.name = "Arial"
#         #font.underline = aw.Underline.DASH

#         # set paragraph formatting
#         paragraphFormat = builder.paragraph_format
#         paragraphFormat.first_line_indent = 8
#         paragraphFormat.alignment = aw.ParagraphAlignment.JUSTIFY
#         paragraphFormat.keep_together = True

#         # add text
#         builder.writeln(data['alt'])  
     
#         '''**NEED TO WORK INTO DOC)this writes alt text to text file, with line numbered by comic'''
#         hover_text = data['alt']
#         number = data['num']


#         with open("images/alt-text.txt", 'a')as f:  #if printing in book this can be skipped
#             f.write(str(number) + ': ' + hover_text + "\n")
#             f.write("\n")
      




# # save document
# doc.save("out.docx")
# '''deletes directory used to store images during process'''  
# shutil.rmtree('images')
