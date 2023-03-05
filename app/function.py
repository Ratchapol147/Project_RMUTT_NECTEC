from pythainlp.tokenize import word_tokenize
import requests
def checkword(con,txt):
     if con.find(txt) > -1: # find indexOf
         return True
     else:
         return False

def countword(txt):
    text_cut = word_tokenize(txt, engine="newmm")
    index = len(text_cut)
    return  index

def calculate(len1,len2):
    # len1 = wordFound
    # len2 = wordnotFound
    try:
        ans = len1 *100 / (len1 + len2)
    except:
        ans = "error"

    return ans

def calculate_word(text,test2):
    wordFound_content =[]
    wordnotFound =[]
    txtlist =[]
    list = word_tokenize(test2, engine="newmm")
    for txt in (list):
        if txt.isspace():
            continue
        elif txt.isascii():
            continue
        else :
         if checkword(text,txt) :
            wordFound_content.append(txt)
         else :
            wordnotFound.append(txt)
            txtlist.append(txt)

    cal = calculate(len(wordFound_content),len(wordnotFound))


    int_wordnotFound=(len(wordnotFound))    
    int_wordFound_content =(len(wordFound_content))

    return wordnotFound,int_wordFound_content,int_wordnotFound,cal

def hightliht(text1,text2):
    txtlist =[]
    i = 0
    # list = word_tokenize(text2, engine="newmm", keep_whitespace=False)
    list = text2.split()
    # list = text2
    ori_text=""
    txt=""
    while i < len(list)  :   
        #print("i ="+str(i))
        txt +=  " " + list[i].strip()
        txt= txt.strip()

        while checkword(text1,txt):
            
            ori_text=txt
            i += 1
            if i >= len(list) :
                break 
            txt +=  " " + list[i].strip()
        #print(txt)
        if i < len(list) :
            txt = list[i].strip() 
            #print('------------>'+txt)
            if  checkword(text1,txt) == -1:
                txt =""
            
        i += 1
        if ori_text =="":
            continue
        txtlist.append(ori_text.strip())
        ori_text= txt
    return txtlist  

def textword(txt):
    for words in txt:

        if words.isspace():
            continue
        elif words.isascii():
            continue
      
    return  words

def delspace(list): #ลบช่องว่างใน list
    out = []
    for ele in list:
        j = ele.replace(' ','')
        out.append(j)
    return out

def repeat_word(list):  #เช็คคำซ้ำ
    v = []
    d = []
    for x in range( len(list) ):
            if list[x] not in v:
                v.append( list[x] )
            else:
                d.append( list[x] )
    
    return v ,d 

def hightlihtforapi(text1,text2):
    txtlist =[]
    i = 0
    ######ทดสอบ
    import requests
 
    url = "https://api.aiforthai.in.th/tlexplus"
    
    params = {'text':text2}
    
    headers = {
        'Apikey': "4VSTV0w7wZEQTY1tV1v126v0gD1BR09W",
        }
    
    response = requests.post(url, params=params, headers=headers)
    
    text = response.json()
    list =(text['tokens'])
    ######ทดสอบ
    # list = word_tokenize(text2, engine="newmm", keep_whitespace=True)
    # print(type(list))
    # list = text2.split()keep_whitespace=False
    # list = text2
    ori_text=""
    txt=""
    while i < len(list)  :   
        #print("i ="+str(i))
        txt +=  " " + list[i].strip()
        txt= txt.strip()

        while checkword(text1,txt):
            
            ori_text=txt
            i += 1
            if i >= len(list) :
                break 
            txt += " " + list[i].strip()
        #print(txt)
        if i < len(list) :
            txt = list[i].strip() 
            #print('------------>'+txt)
            if  checkword(text1,txt) == -1:
                txt =""
            
        i += 1
        if ori_text =="":
            continue
     
        txtlist.append(ori_text.strip())
        ori_text= txt
        
        
    return txtlist  


def fronhightliht(texta,textb,cut):
    # texta = content
    # textb = extractive or  abstractive
    # cut = ข้อความใช้Hight
    colors = ['red' , 'blue']
    countline =0
    for i in  cut :
        countline +=1
        if countline %2:
            texta = texta.replace(i ,'<font color='+colors[1]+'>'+i+'</font>')
            textb = textb.replace(i ,'<font color='+colors[1]+'>'+i+'</font>')
        else:
            texta = texta.replace(i ,'<font color='+colors[0]+'>'+i+'</font>')
            textb = textb.replace(i ,'<font color='+colors[0]+'>'+i+'</font>')

    return texta,textb
