from google_images_search import GoogleImagesSearch
from pathlib import Path
import glob
import os

#Google API Key + Custom Search Engine ID
gis = GoogleImagesSearch('AIzaSyCmMTfEgbsuRXy5aCPClCUZQjMiUULpAIg','003481545842197392659:wucdsj_bptm')

#Specify MAKE|MODEL|YEAR
car = 'honda civic 2018'

#Download Path
download_path = Path("C:/Users/royke/Documents/Coding Projects/IT491/Photos/")

#Search Parameters
gis.search({'q': car, 'num': 1})

#Download image to path and resize
try:
    for image in gis.results():
        image.download(download_path)
        image.resize(500, 500)
    print("Image succesfully downloaded for: " + car)
except:
    print("Unexpected error downloading image")

#Get lastest file from dir
list_of_files = download_path.glob('*')
latest_file = max(list_of_files, key=lambda p: p.stat().st_ctime)

#New File Name
newName = car + '.jpg'

#New File Path
renamed_path = Path("C:/Users/royke/Documents/Coding Projects/IT491/Photos/" + newName)

#Rename file to car name 
os.rename(latest_file, renamed_path)


#More Search Parameters:     
# 'safe': 'high|medium|off'
# 'fileType': 'jpg|gif|png'
# 'imgType': 'clipart|face|lineart|news|photo'
# 'imgSize': 'huge|icon|large|medium|small|xlarge|xxlarge'
# 'searchType': 'image'
# 'imgDominantColor': 'black|blue|brown|gray|green|pink|purple|teal|white|yellow'
