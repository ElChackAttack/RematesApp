from text_to_num import alpha2digit
f = open("{}Remates-12-05-21.txt".format("C:\\Users\\rcrik\\Documents\\RematesApp\\webscrapper\\Remates\\"),'r',encoding='UTF-8')
file_contents = f.read()
print(file_contents)
remates = list(filter(lambda val:val!='',file_contents.split('\n')))
remates_alpha_2_digit_list = [alpha2digit(remate,'es') for remate in remates]
print(remates_alpha_2_digit_list)

