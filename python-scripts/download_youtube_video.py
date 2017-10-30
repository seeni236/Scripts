import webbrowser, sys, pyperclip
import bs4, requests
from selenium import webdriver
import time
import os.path
from pathlib import Path

# link used to implement this code : 
# https://automatetheboringstuff.com/chapter11/

if len(sys.argv) > 1 :
	# Get address from command line
	url = ' '.join(sys.argv[1:])
else :
	# Get address from clipboard.
	url = pyperclip.paste()


download_url = 'https://en.savefrom.net/#url='+url
# new_url = url.replace('youtube', 'ssyoutube')
# type(new_url)
print(download_url)

driver = webdriver.Chrome()
driver.get(download_url)

try : 

	time.sleep(.500)
	home = str(Path.home())
	filenameElement = driver.find_element_by_css_selector('.row.title')
	filename = filenameElement.text+'.mp4'
	print(filename)

	file_path = home+'/Downloads/'+filename
	print(file_path)
	if os.path.exists(file_path): 
		print(file_path+" : File already exists")

	link1 = driver.find_elements_by_class_name('def-btn-name')
	link1[0].click()
	# print('done')
	link2 = driver.find_elements_by_css_selector('.link.link-download.subname.ga_track_events')
	link2[0].click()

	print(os.path.exists(file_path))
	while not os.path.exists(file_path):
	    time.sleep(.300)
	if os.path.isfile(file_path) :
		print('Successfully downloaded')
	else:
		raise ValueError("%s isn't a file!" % file_path)

	
except Exception as ex :
	print('Problem while downloading the video problem :', ex)
	driver.quit()

# driver.quit()