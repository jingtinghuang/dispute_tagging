import csv
import json
import re
import os
from termcolor import colored 


save_dir = "./files/"
files = os.listdir(save_dir)
all_result = dict()
for f in files:
    #print(f)
    with open(save_dir+f) as f:
        data = json.load(f)
    for art in data:
        #print(art)
        all_result[str(art)] = data[str(art)]
        #print(all_result[str(art)])
for index in all_result:

    data = all_result[str(index)]
    is_temp = data["tempting_sentences"]
    if data["tempting_title"]:
        print("title",colored(data["title"]))
    else:
        print("title",data["title"])
    for i in range(len(data["sentences"])):
        if i in is_temp:
            print(i,colored(data["sentences"][i], 'red'))
        else:
            print(i,data["sentences"][i])
    print(data["class"])
    input()
    os.system("clear")

        

    

            
            
        
        
        
    
