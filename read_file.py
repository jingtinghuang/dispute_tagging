import csv
import json
import re
import os 
import argparse
from termcolor import colored 


parser = argparse.ArgumentParser()
parser.add_argument("-s", "--start", help="start",type=int)
parser.add_argument("-e", "--end", help="end",type=int)
args = parser.parse_args()

period_icon = ["；","！","？","。","!",";","?"]
strange_icon = ["&nbsp;","&ldquo;","&rdquo;","&quot;","&hellip;","&mdash;","&lsquo;","&rsquo;"]
append_icon = ["」","）"]
result = dict()
with open("lul.csv","r",encoding="utf-8") as f:
    kk = csv.reader(f)
    count = 0
    for row in kk:
        cleaned_sentences = []
        count += 1
        content = row[1]
        #print(content)
        '''
        for s in strange_icon:
            content = re.sub(s, '', content)
        '''
        content = re.sub(r'\&.*?\;','',content)
        if count <= args.end and count >= args.start:
            temp = ""
            for i in range(len(content)):
                if content[i] not in period_icon:
                    temp += content[i]
                else:
                    temp += content[i]
                    temp = re.sub(r'\s+', '', temp)
                    if temp[0] in period_icon or temp[0] in append_icon:
                        if len(cleaned_sentences) != 0:
                            last = cleaned_sentences[-1]
                            last += temp
                            cleaned_sentences.pop(-1)
                            cleaned_sentences.append(last)
                        else:
                            cleaned_sentences.append(temp)
                    else:
                        cleaned_sentences.append(temp)
                    temp = ""
                


            labels = []
            
            #sentence_list = [x for x in  if len(x) > 0]
            s = 0
            for l in cleaned_sentences:
                s += len(l)

            if len(cleaned_sentences) != 0 and s / (len(cleaned_sentences)) > 10:  
                os.system("clear")
                '''
                print(cleaned_sentences)
                print(s / (len(cleaned_sentences)))
                print(count)
                '''
                this_article = dict()
                print("標題", row[0])
                for i in range(len(cleaned_sentences)):
                    #print("\n")
                    print(i,cleaned_sentences[i])
                keep = input("保留檔案? y/enter: " )
                
                
                if keep != 'y':
                    continue
                class_ = input("輸入分類: ")
                os.system("clear")
                print("開始單句分類!")
                print(row[0])
                title_agg = input("標題是否聳動 y/enter :")
                if title_agg == "y":
                    t_title = True
                else:
                    t_title = False
                for i in range(len(cleaned_sentences)):
                    #print("\n")
                    print(i,cleaned_sentences[i])
                    label = input("是否聳動 y/enter : ")
                    if label == "y":
                        labels.append(i)

                
                os.system("clear")
                change = True
                while change:

                    print(colored("標題", 'red'),colored(t_title, 'yellow') , row[0])
                    for i in range(len(cleaned_sentences)):
                        print(colored(i, 'red'), colored(i in labels, 'yellow'), cleaned_sentences[i])
                    print(class_)
                    
                    change_ = input("修改標記? yes:id or title or class/no:enter ")
                   
                    if len(change_) == 0:
                        change = False
                    else:
                        if not change_.isdigit():
                            if change_ == "title":
                                t_title = not t_title
                            elif change_ == "class":
                                
                                c_class = input("重新輸入分類: ")
                                class_ = c_class
                            else:
                                #print("invalid input",change_,"press enter to countinue")
                                input("invalid input "+str(change_)+" press enter to countinue")

                        else:
                            index = int(change_)
                            if index >= len(cleaned_sentences):
                                #print("invalid index",index,"press enter to countinue")
                                input("invalid index "+str(index)+" press enter to countinue")
                            elif index in labels:
                                labels.remove(index)
                            else:
                                labels.append(index)
                    os.system("clear")



                    
                
                this_article["tempting_title"] = t_title
                this_article["tempting_sentences"] = labels
                this_article["sentences"] = cleaned_sentences
                this_article["title"] = row[0]
                this_article["id"] = count
                this_article["class"] = class_
                result[str(count)] = this_article 


                with open('result'+str(args.start)+'_'+str(args.end)+'.json', 'w') as fp:
                    json.dump(result, fp,ensure_ascii=False)
                


                

        
            #print(len(cleaned_sentences))
        


            
            
        
        
        
    
