# Imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import datetime
from os import getcwd

# Gets current working directory which should be RematesApp
CURRENT_DIRECTORY = getcwd()
print(CURRENT_DIRECTORY)
# Sets options object necessary to add the headless option
options = Options()
# Headless means that browswer window won't be opened but rather just run as a process in the background
options.headless = True
# Creates the driver object which will be used to reach the desired URL
driver = webdriver.Chrome(options=options)
# Desired URL to parse data from
TARGET_URL = "https://www.imprentanacional.go.cr/boletin/"
# Calls the driver to go and visit the desired URL which loads the DOM from which then elements can be parsed
driver.get(TARGET_URL)
# Gets the Webelement/HTML for all auction items available  
# remates = driver.find_element(By.XPATH,"//*[@id='section_2']/div").find_elements(By.XPATH, "//p[preceding-sibling::h2[@id='remates'] and following-sibling::h2[@id='ttulos-supletorios']]")
remates = driver.find_elements(By.XPATH, "//p[preceding-sibling::h2[@id='remates'] and following-sibling::h2[@id='ttulos-supletorios']]")
# List to hold the content for each of the auction items
remates_text = []
# This for loop extracts the actual text from each of the WebElements
for remate in remates:
    remate_text = remate.get_attribute('textContent')
    remate_text = remate_text.replace('\n',' ')
    remates_text.append(remate_text+'\n\n')
    # Console to show that the text extracted is consistent with what is expected
    print("\nRemate text >>> ",remate_text,'\n')

# Get the date for the publication date to create a meaningful name for each of the auction text files
date_string = datetime.datetime.now().strftime("%x").replace('/','-')
# Sanity check for correct date
print(date_string)
f = open("{}\webscrapper\Remates\Remates-{}.txt".format(CURRENT_DIRECTORY,date_string),"w+",encoding="utf-8")
for remate_text_entry in remates_text:
    # f.write(remate_text_entry+'\n\n')
    f.write(remate_text_entry)
    print("Remate >>> {remate}".format(remate=remate_text_entry))
f.close()

# # remates_entries_list = f.open("Remates prueba.txt",'r', encoding="utf-8")