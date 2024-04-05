from typing import Any
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Story(models.Model):
    image = models.FileField(upload_to="static/images", unique=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    content = RichTextField()
    date = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = 'Câu chuyện tình yêu'
        verbose_name_plural = 'Câu chuyện tình yêu'

    def __str__(self):
        return self.title
    
class WendingPersion(models.Model):
    image = models.FileField(upload_to="static/images", unique=True)
    name = models.CharField(max_length=255, verbose_name="Tên (cô dâu hoặc chú rể)", blank=True, null=True)
    dad = models.CharField(max_length=255, blank=True, null=True, verbose_name="Bố")
    mother = models.CharField(max_length=255, blank=True, null=True, verbose_name="Mẹ")
    contetnt = models.TextField(verbose_name="Giới thiệu (cô dâu hoặc chú rể)")
    link = models.TextField(verbose_name="Link liên kết (vd: facebook)")

    class Meta:
        verbose_name = 'Nhân vật cưới'
        verbose_name_plural = 'Nhân vật cưới'

    def __str__(self):
        return self.name
    
class WeddingEvent(models.Model):
    image = models.FileField(upload_to="static/images", unique=True)
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="tiêu đề (vd: Lễ ăn hỏi, tiệc cưới nhà trai/gái,...)")
    date = models.CharField(max_length=255, blank=True, null=True, verbose_name="Thời gian tổ chức sự kiện")
    address = models.CharField(max_length=255, blank=True, null=True, verbose_name="Địa chỉ")
    map = models.TextField(verbose_name="Liên kết bản đồ (google map)", blank=True, null=True)
    order = models.IntegerField(blank=True, null=True, verbose_name="Ưu tiên")

    class Meta:
        verbose_name = 'Sự kiện tiệc cưới'
        verbose_name_plural = 'Sự kiện tiệc cưới'
    
    def __str__(self) -> str:
        return self.title


    




