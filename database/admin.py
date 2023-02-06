from django.contrib import admin
from database.models import datafull,txtsum

class datafullAdmin(admin.ModelAdmin):
    list_display=['id','news_author','news_title','news_content','news_counttext','news_datepublish','date_addtostored','extractive','abstractive']
admin.site.register(datafull,datafullAdmin) 

class textsumAdmin(admin.ModelAdmin):
    list_display=['id','content','abstractive','extractive']
admin.site.register(txtsum,textsumAdmin)

