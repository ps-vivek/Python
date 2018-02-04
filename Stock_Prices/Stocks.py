'''
Parse around 20 files in a directory that contain the stock prices and other details related to a company.
Process the stock prices alone and display the following details:
1) Maximum stock price 2) Maximum stock price Date 
2) Minimum stock price 2) Minimum stock price date    
'''

import os
from fnmatch import fnmatch

file_names=list()
sp_dict=dict() #s_p => stock price

for path, subdirs, files in os.walk(os.getcwd()):
    for name in files:
        if fnmatch(name,"*.txt"):
            file_names.append(path+"\\"+name) #writing the names of all the files into a list

count=0
for names in file_names:
    fh=open(names)
    for line in fh:
        if not line.startswith("Date: "): #following is the format of date format in the files
            continue                      #Date:   1/26/2015	CompanyName	  Cost:$64.35
        words= (line.split())             #words[0]  words[1]    words[2]   words[3]   words[4]
                                          #splitting the lines based on space
        date=words[1].split("/")          #Splitting the dates to get individual month, date and year
        #print (date[0]) #month
        #print (date[1]) #date
        #print (date[2]) #year
        if int(date[0]) < 10:         #if month is less than october, add a '0' to the month # Helps in sorting
            date[0]='0'+date[0]

        if int(date[1]) < 10:         #if date is less than 10, add a '0' to the date # helps in sorting
            date[1]='0'+date[1]

        dates=[date[2],date[0],date[1]] #write the date in year, month, date format. helps in sorting
        print (dates)
        dat="".join(dates) #joining year, month, date into a single variable. Helpful for sorting

        price=words[4].split(":") #splitting out. For instance "Cost:$64.35" into Cost & $64.35
        pr_i=price[1].find('$') #finding the index where the "$" character starts
        sp=price[1][pr_i+1:] #sp=>stock price

        if not dat in sp_dict:
            sp_dict[dat]=sp    #adding date and stock price to the dictionary

sp_list=list()
for dat,sp in sp_dict.items():
    sp_list.append((dat,sp))  #appending dat and sp to a new list

sp_list.sort()
max=0.0
min=99999.9

for i in sp_list: #iterating through list of tuples
    if float(i[1]) > max:
        max=float(i[1]) #max stock price
        max_date=i[0]   #max stock date

    if float(i[1]) < min:
        min=float(i[1]) #min stock price
        min_date=i[0]   #min stock date

print ("Max stock price:",max,"Max date:",max_date)
print ("Min stock price:",min,"Min date:",min_date)