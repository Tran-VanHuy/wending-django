from django.db import models
from ckeditor.fields import RichTextField
from .enums import *
from django.utils.safestring import mark_safe


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
    
class AlbumWedding(models.Model):
    image = models.FileField(upload_to="static/images", unique=True, verbose_name="Ảnh nhỏ (hiển thị ở ngoài trang chủ)")
    image_large = models.FileField(upload_to="static/images", unique=True, verbose_name="Ảnh lớn (hiển thị trong slide)", blank=True, null=True)
    type = models.IntegerField(
        unique=True,
        choices=[
            (AlbumEnums.image_1.value, 'Ảnh 1'),
            (AlbumEnums.image_2.value, 'Ảnh 2'),
            (AlbumEnums.image_3.value, 'Ảnh 3'),
            (AlbumEnums.image_4.value, 'Ảnh 4'),
            (AlbumEnums.image_5.value, 'Ảnh 5'),
            (AlbumEnums.image_6.value, 'Ảnh 6'),
            (AlbumEnums.image_7.value, 'Ảnh 7'),
            (AlbumEnums.image_8.value, 'Ảnh 8'),
            (AlbumEnums.image_9.value, 'Ảnh 9'),
            (AlbumEnums.image_10.value, 'Ảnh 10'),
            (AlbumEnums.image_11.value, 'Ảnh 11'),
        ],
        verbose_name="Vị trí ảnh"
    )

    class Meta:
        verbose_name = "Album ảnh tiệc cưới"
        verbose_name_plural = "Album ảnh tiệc cưới"
    
    def __str__(self):
        return mark_safe(f'<img src="/{self.image}" style="width: 100px; height: 100px" /> - Vị trí ảnh: {self.type}')


class Banner(models.Model):
    image = models.FileField(upload_to="static/images", unique=True, verbose_name="Banner hiển thị ở trang chủ")
    location = models.IntegerField(
        choices=[
            (LocationBannerEnums.location_banner_1.value, 'Vị trí 1'),
            (LocationBannerEnums.location_banner_2.value, 'Vị trí 2'),
            (LocationBannerEnums.location_banner_3.value, 'Vị trí 3'),
            (LocationBannerEnums.location_banner_4.value, 'Vị trí 4')
        ],
        verbose_name="Vị trí",
        blank=True,
        null=True
    )

    def __str__(self):
        return mark_safe(f'<img src="/{self.image}" style="width:100px; height: 100px" />')

class GuestbookNumber(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    content = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name="Sổ lưu bút"
        verbose_name_plural = "Sổ lưu bút"


    




