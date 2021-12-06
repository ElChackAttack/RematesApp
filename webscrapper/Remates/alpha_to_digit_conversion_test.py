from text_to_num import alpha2digit
import datetime
# TILDES_MAP = {'á':'a','é':'',íóú}
# íóú iou
f = open("{}Remates-12-05-21.txt".format("C:\\Users\\rcrik\\Documents\\RematesApp\\webscrapper\\Remates\\"),'r',encoding='UTF-8')
file_contents = f.read()
f.close()
remates = list(filter(lambda val:val!='',file_contents.lower().split('\n')))
remates = [remate.replace('á','a').replace('é','e').replace('í','i').replace('ó','o').replace('ú','u') for remate in remates]
remates_alpha_2_digit_list = [alpha2digit(remate,'es') for remate in remates]
print(remates_alpha_2_digit_list)
date_string = datetime.datetime.now().strftime("%x").replace('/','-')
f = open("{}Remates-{}-alpha2digit.txt".format("C:\\Users\\rcrik\\Documents\\RematesApp\\webscrapper\\Remates\\",date_string),'w+',encoding='UTF-8')
for remate in remates_alpha_2_digit_list:
    f.write(remate+'\n')
f.close()