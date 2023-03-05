import json
from urllib import request
from django.shortcuts import render
from rest_framework import parsers
from .serializers import datafullSerializer,txtsumSerializer
from database.models import datafull,txtsum
from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser
from  app.function import textword,countword,hightliht,delspace,repeat_word,hightlihtforapi,fronhightliht,calculate_word
from pythainlp.tokenize import word_tokenize
from django.utils.datastructures import MultiValueDictKeyError



#--------------------ออกมาเยอะเกินค้าง Haha -----------------------------
class datafullList(generics.ListAPIView):
    queryset = datafull.objects.all()
    serializer_class = datafullSerializer

class txtsumlList(generics.ListAPIView):
    queryset = txtsum.objects.all()
    serializer_class = txtsumSerializer
#-------------------------------------------------
#---------------------เลือก ID ----------------------------

class datafullDetail(generics.RetrieveAPIView):
    queryset = datafull.objects.all()
    serializer_class = datafullSerializer
    permission_classes = [permissions.IsAuthenticated]
class txtsumDetail(generics.RetrieveAPIView):
    queryset = txtsum.objects.all()
    serializer_class = txtsumSerializer
    permission_classes = [permissions.IsAuthenticated]

#-------------------------------------------------  RetrieveUpdateDestroyAPIView

def api(request):
   
    
    return render(request,'api.html')




class ApiView(APIView):
    
    """
    similarity = เปอร์เช็นความเหมือน 
    similarityWord = คำที่เหมือนกัน
    Cutworddata1 = การตัดคำ
    Cutworddata2 = การตัดคำ
    HTMLTag1 = ส่วนแสดง Tag HTML:5

    """
    
    
    def post(self, request):

        print(self.request)
        data1 =request.data['data1']
        data2 =request.data['data2']
        

        wordnotFound_data,int_wordFound_content_data,int_wordnotFound_data,cal_data = calculate_word(data1,data2)

    
    
        b1=word_tokenize(data1,engine='newmm')
        b2=word_tokenize(data2,engine='newmm')
        
        lendata1 = len(b1)
        lendata2 = len(b2)


        testsum = hightlihtforapi(data1,data2)

        res = delspace(testsum)
        sorted_data = (sorted(res,key = len, reverse=True))
        a ,b = repeat_word(sorted_data)

        hig1,hig2=fronhightliht(data1,data2,a)
        

        
        request.data['similarity'] = cal_data
        request.data['similarityWord'] = testsum
        request.data['Cutworddata1'] = b1
        request.data['Cutworddata2'] = b2
        request.data['countworddata1'] = lendata1
        request.data['countworddata2'] = lendata2
        request.data['HTMLTag1'] = hig1
        request.data['HTMLTag2'] = hig2

          


        return Response(
            {
            'status': status.HTTP_200_OK,
            'data': request.data
            
           
            }
        )
class ApiinDB(APIView):
        """
        API call in Database
        """
        def post(self,request):

            # id =int(request.data['input'])
            try: id = int(request.data['input'])
            except MultiValueDictKeyError:
                id = 1
        
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

            request.data['text_content_def'] = text_content_datafull_ext,
            request.data['text_extractive_def'] = text_extractive_datafull,
            #========
            request.data['text_content_datafull_abs'] = text_content_datafull_abs,
            request.data['text_abstractive_datafull'] = text_abstractive_datafull,
            #===============================================
            request.data['id'] = id,
            request.data['progress'] = progress,
            #========
            request.data['wordnotFound_ext'] = wordnotFound_ext,
            request.data['int_wordFound_content_ext'] = int_wordFound_content_ext,
            request.data['int_wordnotFound_ext'] = int_wordnotFound_ext,
            #========
            request.data['wordnotFound_abs'] = wordnotFound_abs,
            request.data['int_wordFound_content_abs'] = int_wordFound_content_abs,
            request.data['int_wordnotFound_abs'] = int_wordnotFound_abs,
            #========
            request.data['count_word_con'] = count_word_con,
            #========
            request.data['count_word_ext'] = count_word_ext,
            #========
            request.data['count_word_abs'] = count_word_abs,
            #========
            request.data['labels_ext'] = labels_ext,
            request.data['labels_abs'] = labels_abs,
            request.data['data_ext'] = data_ext,
            request.data['data_abs'] = data_abs,

            return Response(
            {
            'data': request.data
             }
        )

        
            
           
            
        

    
