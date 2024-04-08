from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *
from .enums import *
from .forms import *


# Create your views here.

class Index(TemplateView):
    template_name = "index.html"
    form_class = GuestbookNumberForm

    def get_context_data(self, **kwargs: Any):

        context = super().get_context_data(**kwargs)

        story = Story.objects.all()
        wendingPersion = WendingPersion.objects.all().order_by('-id')
        weddingEvent = WeddingEvent.objects.all().order_by('id')
        album1 = AlbumWedding.objects.filter(type=AlbumEnums.image_1.value).first()
        album2 = AlbumWedding.objects.filter(type=AlbumEnums.image_2.value).first()
        album3 = AlbumWedding.objects.filter(type=AlbumEnums.image_3.value).first()
        album4 = AlbumWedding.objects.filter(type=AlbumEnums.image_4.value).first()
        album5 = AlbumWedding.objects.filter(type=AlbumEnums.image_5.value).first()
        album6 = AlbumWedding.objects.filter(type=AlbumEnums.image_6.value).first()
        album7 = AlbumWedding.objects.filter(type=AlbumEnums.image_7.value).first()
        album8 = AlbumWedding.objects.filter(type=AlbumEnums.image_8.value).first()
        album9 = AlbumWedding.objects.filter(type=AlbumEnums.image_9.value).first()
        album10 = AlbumWedding.objects.filter(type=AlbumEnums.image_10.value).first()
        album11 = AlbumWedding.objects.filter(type=AlbumEnums.image_11.value).first()
        banner1 = Banner.objects.filter(location=LocationBannerEnums.location_banner_1.value).first()
        banner2 = Banner.objects.filter(location=LocationBannerEnums.location_banner_2.value).first()
        banner3 = Banner.objects.filter(location=LocationBannerEnums.location_banner_3.value).first()
        banner4 = Banner.objects.filter(location=LocationBannerEnums.location_banner_4.value).first()
        guestbook_mumber = GuestbookNumber.objects.all()

        context['story'] = story
        context['wendingPersion'] = wendingPersion
        context['weddingEvent'] = weddingEvent
        context['album1'] = album1
        context['album2'] = album2
        context['album3'] = album3
        context['album4'] = album4
        context['album5'] = album5
        context['album6'] = album6
        context['album7'] = album7
        context['album8'] = album8
        context['album9'] = album9
        context['album10'] = album10
        context['album11'] = album11
        context['banner1'] = banner1
        context['banner2'] = banner2
        context['banner3'] = banner3
        context['banner4'] = banner4
        context['guestbook_mumber'] = guestbook_mumber
        context['form'] = self.form_class()

        return context
    
    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()
        
        return self.render_to_response(context)


class Xntd(TemplateView):
    template_name = "xntd.html"
