from django.db import models

class datafull (models.Model):
    # news_author สำนักพิมพ์
    # news_title หัวข้อข่าว
    # news_content เนื้อหาข่าว
    # news_counttext จำนวนตัวหนังสือเขื้อหาข่าว
    # news_site เว็ปไซต์ข่าว
    # news_link ลิงค์
    # news_datepublish วันที่เผยแพร่
    # date_addtostored ไม่รู้คือไร!!
    # extractive   เรียบเรียงใหม่
    # abstractive  เรียงเรียงจากข่าวต้นฉบับ

    news_author = models.TextField(null=True, blank=True)
    news_title = models.TextField(null=True, blank=True)
    news_content = models.TextField(null=True, blank=True)
    news_counttext = models.TextField(null=True, blank=True)
    news_datepublish = models.TextField(null=True, blank=True)
    date_addtostored = models.TextField(null=True, blank=True)
    extractive = models.TextField(null=True, blank=True)
    abstractive = models.TextField(null=True, blank=True)

class txtsum(models.Model):
    content = models.TextField(null=True, blank=True)
    abstractive = models.TextField(null=True,blank=True)
    extractive = models.TextField(null=True, blank=True)
