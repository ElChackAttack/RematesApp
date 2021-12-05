# Imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import datetime

# Sets options object necessary to add the headless option
options = Options()
# Headless means that browswer window won't be opened but rather just run as a process in the background
options.headless = True
# Creates the driver object which will be used to reach the desired URL
driver = webdriver.Chrome(options=options)
# Desired URL to parse data from
TARGET_URL = "https://www.imprentanacional.go.cr/boletin/"
driver.get(TARGET_URL)

remates = driver.find_element(By.XPATH,"//*[@id='section_2']/div").find_elements(By.XPATH, "//p[preceding-sibling::h2[@id='remates'] and following-sibling::h2[@id='avisos']]")

remates_text = []
for remate in remates:
    remate_text = remate.get_attribute('textContent')
    remate_text = remate_text.replace('\n',' ')
    remates_text.append(remate_text+'\n\n')
    print("\nRemate text >>> ",remate_text,'\n')


date_string = datetime.datetime.now().strftime("%x").replace('/','-')
print(date_string)
f = open("Remates-{}.txt".format(date_string),"w+",encoding="utf-8")
for remate_text_entry in remates_text:
    # f.write(remate_text_entry+'\n\n')
    f.write(remate_text_entry)
    print("Remate >>> {remate}".format(remate=remate_text_entry))
f.close()

# # remates_entries_list = f.open("Remates prueba.txt",'r', encoding="utf-8")