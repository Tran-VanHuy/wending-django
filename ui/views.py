from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *


# Create your views here.

class Index(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs: Any):

        context = super().get_context_data(**kwargs)
        story = Story.objects.all()
        wendingPersion = WendingPersion.objects.all().order_by('-id')
        weddingEvent = WeddingEvent.objects.all().order_by('id')
        context['story'] = story
        context['wendingPersion'] = wendingPersion
        context['weddingEvent'] = weddingEvent
        return context

class Xntd(TemplateView):
    template_name = "xntd.html"
