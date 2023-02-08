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
class txtsumDetail(generics.RetrieveAPIView):
    queryset = txtsum.objects.all()
    serializer_class = txtsumSerializer


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

        print(wordnotFound_data)
        print(int_wordFound_content_data)
        print(int_wordnotFound_data)
        print(cal_data)
    
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

    
