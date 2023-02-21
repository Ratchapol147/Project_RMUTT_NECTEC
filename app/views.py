from django.shortcuts import render ,redirect
from database.models import datafull,txtsum
from .function import textword,countword,hightliht,delspace,repeat_word,calculate_word,fronhightliht
from django.utils.datastructures import MultiValueDictKeyError
from pythainlp.tokenize import word_tokenize
import requests
import json

def home(request):
    return render(request,'frontend/index.html')




def process(request):
        try: num1 = int(request.GET['search'])
        except MultiValueDictKeyError:
            num1 = 1
        id = num1
        data_datafull = datafull.objects.get(id=id)
        data_txtsim   = txtsum.objects.get(id=id)
        text_content_datafull = data_datafull.news_content
        text_abstractive_datafull = data_datafull.abstractive
        text_extractive_datafull = data_datafull.extractive

        text_content = data_txtsim.content
        text_abstractive = data_txtsim.abstractive
        text_extractive = data_txtsim.extractive

  

        
        hightlihttext_ext = hightliht(text_content,text_extractive)
        hightlihttext_abs = hightliht(text_content,text_abstractive)
        
        res_ext = delspace(hightlihttext_ext)
        res_abs = delspace(hightlihttext_abs)

        sorted_data_ext = (sorted(res_ext,key = len, reverse=True))
        sorted_data_abs = (sorted(res_abs,key = len, reverse=True))


        count_word_con =countword(text_content_datafull)
        count_word_ext =countword(text_extractive_datafull)
        count_word_abs =countword(text_abstractive_datafull)

        wordnotFound_abs,int_wordFound_content_abs,int_wordnotFound_abs,cal_abs = calculate_word(text_content_datafull,text_abstractive_datafull) #abstractive
        wordnotFound_ext,int_wordFound_content_ext,int_wordnotFound_ext,cal_ext = calculate_word(text_content_datafull,text_extractive_datafull) #extractive
        
        a_ext ,b_ext = repeat_word(sorted_data_ext) 
        a_abs ,b_abs = repeat_word(sorted_data_abs) 
        # a ลบตัวซ้ำในข้อมูล
        # b ข้อมู,ที่ซ้ำในข้อมูล

        progress1 = (id/3190)*100
        progress = round(progress1)
        
        text_content_datafull_ext,text_extractive_datafull=fronhightliht(text_content_datafull,text_extractive_datafull,a_ext)
        text_content_datafull_abs,text_abstractive_datafull=fronhightliht(text_content_datafull,text_abstractive_datafull,a_abs)
       

        new_data_abs = round(cal_abs)
        new_data_ext = round(cal_ext)
        
        
        labels_ext =["Extractive"]
        labels_abs =["Abstractive"]
        data_ext =[new_data_ext]
        data_abs =[new_data_abs]

        return render(request,'frontend/process-page.html',{
            'text_content_def':text_content_datafull_ext,
            'text_extractive_def':text_extractive_datafull,
            #========
            'text_content_datafull_abs':text_content_datafull_abs,
            'text_abstractive_datafull':text_abstractive_datafull,
            #===============================================
            'id':id,
            'progress':progress,
            #===============================================
            'wordnotFound_ext':wordnotFound_ext,
            'int_wordFound_content_ext':int_wordFound_content_ext,
            'int_wordnotFound_ext':int_wordnotFound_ext,
            #========
            'wordnotFound_abs':wordnotFound_abs,
            'int_wordFound_content_abs':int_wordFound_content_abs,
            'int_wordnotFound_abs':int_wordnotFound_abs,
            #===============================================
            'count_word_con':count_word_con,
            #========
            'count_word_ext':count_word_ext,
            #========
            'count_word_abs':count_word_abs,
            #===============================================
            'labels_ext':labels_ext,
            'labels_abs':labels_abs,
            'data_ext':data_ext,
            'data_abs':data_abs,
        })

def input_process(request):
    if request.method == 'POST':
      
        
        if(request.method == 'POST'):
            data1 = request.POST['data1']
            data2 = request.POST['data2']


            url = "http://127.0.0.1:8000/api/test/"

            payload = json.dumps({
            "data1": data1,
            "data2": data2
            })
            headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Basic YWRtaW46b2htMTMxMTI1MjM='
            }

            response = requests.request("POST", url, headers=headers, data=payload)
            response = response.json()
            data = response['data']

            # similarity = เปอร์เช็นความเหมือน 
            # similarityWord = คำที่เหมือนกัน
            # Cutworddata1 = การตัดคำ
            # Cutworddata2 = การตัดคำ
            # HTMLTag1 = ส่วนแสดง Tag HTML:5
            # countworddata2 = แสดงจำนวนคำ
            

            similarity =data['similarity']
            similarityWord =data['similarityWord']
            Cutworddata1 =data['Cutworddata1']
            Cutworddata2=data['Cutworddata2']
            countworddata1= data['countworddata1']
            countworddata2 =data['countworddata2']
            HTMLTag1 =data['HTMLTag1']
            HTMLTag2 =data['HTMLTag2']
            lenword = (len(similarityWord))
  
         
        return render(request,'frontend/process_input.html',{
            'similarity':similarity,
            'lenword':lenword,
            'similarityWord':similarityWord,
            'Cutworddata1':Cutworddata1,
            'Cutworddata2':Cutworddata2,
            'countworddata1':countworddata1,
            'countworddata2':countworddata2,
            'HTMLTag1':HTMLTag1,
            'HTMLTag2':HTMLTag2,
        })
    else:
        return render(request,'frontend/process_input.html')




