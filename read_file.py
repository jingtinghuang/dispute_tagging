import csv
import json
import re
import os 

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
        if count <= 1280 and count >= 1200:
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
                os.system("clear")
                if keep != 'y':
                    continue
                print("開始單句分類!")
                print(row[0])
                title_agg = input("標題是否聳動 y/enter :")
                if title_agg == "y":
                    this_article["tempting_title"] = True
                else:
                    this_article["tempting_title"] = False
                for i in range(len(cleaned_sentences)):
                    #print("\n")
                    print(i,cleaned_sentences[i])
                    label = input("是否聳動 y/enter : ")
                    if label == "y":
                        labels.append(i)
                class_ = input("輸入分類: ")
                this_article["tempting_sentences"] = labels
                this_article["sentences"] = cleaned_sentences
                this_article["title"] = row[0]
                this_article["id"] = count
                this_article["class"] = class_
                result[str(count)] = this_article 
                with open('result.json', 'w') as fp:
                    json.dump(result, fp,ensure_ascii=False)
                os.system("clear")


                

        
            #print(len(cleaned_sentences))
        


            
            
        
        
        
    
