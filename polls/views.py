# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse


# Create your views here, this is essentially your controller code
def index(request):
    return HttpResponse("Hello world. You're at the polls index.")
