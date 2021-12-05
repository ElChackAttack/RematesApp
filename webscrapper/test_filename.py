import datetime

date_string = datetime.datetime.now().strftime("%x").replace('/','\/')
print(date_string)
f=open('{}.txt'.format(date_string),'w+')
f.close()