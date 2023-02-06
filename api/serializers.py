from rest_framework import serializers
from  database.models import txtsum,datafull 


class txtsumSerializer(serializers.ModelSerializer):

    class Meta:
        
        fields = ('id', 'content', 'abstractive', 'extractive')
        model = txtsum

class datafullSerializer(serializers.ModelSerializer):

    class Meta:
        
        fields = ('id', 'news_author', 'news_title', 'news_content', 'news_counttext', 'news_datepublish', 'date_addtostored', 'extractive', 'abstractive')
        model = datafull

